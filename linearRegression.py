# for performing matrix operations
import numpy as np
# for saving plots etc.
import matplotlib.pyplot as plt
# get the dataframe from the createDataFrame file
from createDataFrame import df
# we will use the os module to create the
# the directory to store the files to
import os

def linearRegression():

    # I adapted the code for creating a directory
    # if it doesn't already exist from here:
    # https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory
    # first we get the absolute path of the current directory
    # by calling the dirname() method on the os module's path
    # field with a parameter of the current filename
    # (represented by the 'dunder' or 'magic' __file__
    # variable that is built into Python).
    scriptDir = os.path.dirname(__file__)
    # we then create the path of the new directory by calling
    # the join() method on the os module's path field with two
    # parameter, the first being the current directory's path, and the
    # second being the subdirectory we want to add to it.
    plotDir = os.path.join(scriptDir, 'plots/linearRegression/')
    # we then check if the directory we want to create already
    # exists, and only if it doesn't exist do we invoke the os
    # module's makedirs() method to create it.
    if not os.path.isdir(plotDir):
        os.makedirs(plotDir)

    # dataframe.mean() returns a series object, we want
    # to change this to a list with the series.tolist() method.
    means = df.mean().tolist()
    # we now remove the species column from the dataframe
    variablesMatrix = df.iloc[:, :4]
    # to create the 'means matrix' we create a matrix
    # the same size as the variable matrix but filled with ones
    meansMatrix = np.ones((150, 4))
    # we then simply multiply this matrix of ones by the list
    # of means.
    meansMatrix *= means
    # subtracting the means matrix from the variables matrix
    # gives us the zero-centred matrix
    zeroCentredMatrix = variablesMatrix - meansMatrix
    # now multiply the variablesMatrix but its transposition
    transpositionMatrixByVariablesMatrix = variablesMatrix.transpose() @ variablesMatrix
    # to create the 'means product matrix' we multiply the transpose
    # of the means by the untransposed matrix of means - note that
    # this is element-wise rather than matrix multiplication
    meansProductMatrix = np.array([means]).T * np.array([means])
    # we now multiply this matrix by the scalar, number of instances
    nMeansProductMatrix = 150 * meansProductMatrix
    # to get the scatter matrix we subtract the above matrix from the
    # transpositionMatrixByVariablesMatrix
    scatterMatrix = transpositionMatrixByVariablesMatrix - nMeansProductMatrix
    # to get the covariance matrix we divide the scatter matrix by the scalar,
    # number of instances
    covarianceMatrix = (1 / 150) * scatterMatrix
    # we now want to check that the difference between the values in
    # our covariance matrix and the matrix as calculated by Pandas itself
    # is not significant. We can do this by
    # calculating the mean difference between the covariance matrix
    # values as calculated here and as calculated by Pandas cov()
    # method. We do this by calling Dataframe.mean on the dataframe,
    # which will return a series object of the mean for each column,
    # and then calling series.mean will return the mean of these means.
    # we want to make sure the difference is less than 0.01, so we call
    # abs() on the number.
    assert abs(((covarianceMatrix - df.cov()).mean()).mean()) < 0.01
    # to get the correlation matrix we first need to calculate the
    # standard deviation of each feature.
    stds = df.std().tolist()

    correlationMatrix = covarianceMatrix.copy()
    # we now divide the covariances by the produce of the variables
    # standard deviation. This can be done manually with nested for loops.
    for i in range(len(covarianceMatrix)):
        for j in range(len(stds)):
            x = covarianceMatrix.iloc[i][j]
            y =  stds[i]
            correlationMatrix.iloc[i][j] /= (stds[i] * stds[j])
    # we now check that this matches with Pandas own calculation
    assert abs(((correlationMatrix - df.corr()).mean()).mean()) < 0.01
    # we can go a step further and calculate a 'determination' matrix
    # by squaring the correlation coefficients
    determinationMatrix = correlationMatrix.copy()
    for i in range(len(determinationMatrix)):
        for j in range(len(determinationMatrix)):
            determinationMatrix.iloc[i][j] *= determinationMatrix.iloc[i][j]


    # calculate the regression coefficient where petal length is the
    # explanatory variable and petal width is the dependent variable

    regressionCoefficient = covarianceMatrix.iloc[2][3] / covarianceMatrix.iloc[2][2]
    yIntercept = means[3] - regressionCoefficient * means[2]

    # because the slope of a straight line does not change, we only
    # need to use two two y values as predicted by the linear regression
    # equation to plot the line, namely, those predicted from the lowest
    # and highest values of x respectively
    predictedY = [yIntercept + regressionCoefficient * df['petal_length'].min(), yIntercept + regressionCoefficient * df['petal_length'].max()]

    ax = plt.subplot(1,1,1)
    for label, group in df.groupby("species"):
        plt.plot(group["petal_length"], group["petal_width"], '.', label=label)
    plt.plot([df['petal_length'].min(), df['petal_length'].max()], predictedY)
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Linear Regression of Petal Length vs. Petal Width")
    plt.grid()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.savefig(plotDir + "linearRegressionPetalLengthPetalWidth.png")
    plt.close()


if __name__ == '__main__':
    linearRegression()
