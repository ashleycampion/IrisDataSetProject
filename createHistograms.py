# we want numpy for creating numpy arrays with linspace
# method. Linspace can easily create arrays with steps
# of floating point magnitudes, which will be needed
# to specify the bins for the histograms.
import numpy as np
# for creating the actual histograms we want matplotlib.pyplot
import matplotlib.pyplot as plt
# get the dataframe from the createDataFrame file
from createDataFrame import df
# import the indices that will allow us create separate plots
# for each of the species (for more on how this is achieved
# see comments in createDataFrame file)
from createDataFrame import versicolor
from createDataFrame import virginica

# this function will be called by the main analysis file
def createHistograms():

    # first create histograms for each variable except species
    # where all species are lumped together

    # the steps for creating the histograms are the same for each
    # variable plotted, so I will annotate the process only once.
    # First plot the histogram with the appropriate array. The second
    # paramater here specifies the width and range of the bins. I have
    # decided not to vary this across the histograms. While this
    # is not ideal in the sense that there will be a lot of 'white
    # space' on most of the histograms, I think this is made up for
    # by the ease with which one can compare the histograms, i.e. one
    # does not have to factor in the range of the bins but can compare
    # the variables and species purely by looking at the plots.
    # 8 is the upper bound (virginica sepal length) and 0 is the lower
    # (setosa petal width). While bins of 0.25 width are probably the
    # most visually appealing, the setosa-petal values are clumped
    # together so much that histograms with a width of 0.5 really aren't
    # granular enough. Bins of 0.125 have been used instead.
    # but the setosa petal lengths and widths
    plt.hist(df["sepal_length"], bins=np.linspace(0,8,64))
    # we now include the label for the x axis
    plt.xlabel("Sepal Length (cm)")
    # and the y axis
    plt.ylabel("Occurences")
    # give the plot its title
    plt.title("Sepal Length")
    # save it to a file in the plots/histogram folder
    plt.savefig("plots/histograms/sepalLength.png")
    # and close the plot so that the next plot is not
    # superimposed on top of this one
    plt.close()

    plt.hist(df["sepal_width"], bins=np.linspace(0,8,64))
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Occurences")
    plt.title("Sepal Width")
    plt.savefig("plots/histograms/sepalWidth.png")
    plt.close()

    plt.hist(df["petal_length"], bins=np.linspace(0,8,64))
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Occurences")
    plt.title("Petal Length")
    plt.savefig("plots/histograms/petalLength.png")
    plt.close()

    plt.hist(df["petal_width"], bins=np.linspace(0,8,64))
    plt.xlabel("Petal Width (cm)")
    plt.ylabel("Occurences")
    plt.title("Petal Width")
    plt.savefig("plots/histograms/petalWidth.png")
    plt.close()

    # setosa
    plt.hist(df["sepal_length"][:versicolor], bins=np.linspace(0,8,64))
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Occurences")
    plt.title("Setosa Sepal Length")
    plt.savefig("plots/histograms/setosaSepalLength.png")
    plt.close()

    plt.hist(df["sepal_width"][:versicolor], bins=np.linspace(0,8,64))
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Occurences")
    plt.title("Setosa Sepal Width")
    plt.savefig("plots/histograms/setosaSepalWidth.png")
    plt.close()

    plt.hist(df["petal_length"][:versicolor], bins=np.linspace(0,8,64))
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Occurences")
    plt.title("Setosa Petal Length")
    plt.savefig("plots/histograms/setosaPetalLength.png")
    plt.close()

    plt.hist(df["petal_width"][:versicolor], bins=np.linspace(0,8,64))
    plt.xlabel("Petal Width (cm)")
    plt.ylabel("Occurences")
    plt.title("Setosa Petal Width")
    plt.savefig("plots/histograms/setosaPetalWidth.png")
    plt.close()

    # versicolor
    plt.hist(df["sepal_length"][versicolor:virginica], bins=np.linspace(0,8,64))
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Occurences")
    plt.title("Versicolor Sepal Length")
    plt.savefig("plots/histograms/versicolorSepalLength.png")
    plt.close()

    plt.hist(df["sepal_width"][versicolor:virginica], bins=np.linspace(0,8,64))
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Occurences")
    plt.title("Versicolor Sepal Width")
    plt.savefig("plots/histograms/versicolorSepalWidth.png")
    plt.close()

    plt.hist(df["petal_length"][versicolor:virginica], bins=np.linspace(0,8,64))
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Occurences")
    plt.title("Versicolor Petal Length")
    plt.savefig("plots/histograms/versicolorPetalLength.png")
    plt.close()

    plt.hist(df["petal_width"][versicolor:virginica], bins=np.linspace(0,8,64))
    plt.xlabel("Petal Width (cm)")
    plt.ylabel("Occurences")
    plt.title("Versicolor Petal Width")
    plt.savefig("plots/histograms/versicolorPetalWidth.png")
    plt.close()

    # virginica
    plt.hist(df["sepal_length"][virginica:], bins=np.linspace(0,8,64))
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Occurences")
    plt.title("Virginica Sepal Length")
    plt.savefig("plots/histograms/virginicaSepalLength.png")
    plt.close()

    plt.hist(df["sepal_width"][virginica:], bins=np.linspace(0,8,64))
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Occurences")
    plt.title("Virginica Sepal Width")
    plt.savefig("plots/histograms/virginicaSepalWidth.png")
    plt.close()

    plt.hist(df["petal_length"][virginica:], bins=np.linspace(0,8,64))
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Occurences")
    plt.title("Virginica Petal Length")
    plt.savefig("plots/histograms/virginicaPetalLength.png")
    plt.close()

    plt.hist(df["petal_width"][virginica:], bins=np.linspace(0,8,64))
    plt.xlabel("Petal Width (cm)")
    plt.ylabel("Occurences")
    plt.title("Virginica Petal Width")
    plt.savefig("plots/histograms/virginicaPetalWidth.png")
    plt.close()
