# for creating the actual scatter plots we want matplotlib.pyplot
import matplotlib.pyplot as plt

# we will use pandas groupby() function to group by species
# when plotting the variables against each other
import pandas as pd

# we will use seaborn pairplot() to present all of the plots
# on one image file
import seaborn as sb

# get the dataframe from the createDataFrame file
from createDataFrame import df
# import the indices that will allow us create separate plots
# for each of the species (for more on how this is achieved
# see comments in createDataFrame file)
#from createDataFrame import versicolor
#from createDataFrame import virginica

# this function will be called by the main analysis file
def createScatterPlots():

    # there is really no reason when creating scatter plots
    # based on the iris dataset not to distinguish between
    # each of the three variables. When, for example, comparing
    # petal length and petal width, there is no disadvantage
    # to coloring the plots according to the species rather
    # than having a monochromatic plot, and the trends of the
    # variables in the iris data set are clearly related to the
    # species, so by coloring the plots based on the species
    # we can more clearly see the trends and compares how the
    # trends for each species differ. This function then plots
    # the lengths and widths against each other and adding
    # colour to distinguish the species, and also plots the species
    # against all of the lengths and widths

    # we could have used the scatter() function for these plots,
    # but the plot() function works just as well for our use,
    # and is quicker, as demonstrated here:
    # https://pythonmatplotlibtips.blogspot.com/2018/01/compare-pltplot-and-pltscatter-in-speed-python-matplotlib.html

    # I have not included the grid to these scatter plots, as
    # I think it is distracting.

    # to plot each of the species against the other variable
    # really isn't very interesting; I have only included
    # these plots here for completeness.
    # species vs other-variables plots

    # for the third parameter to the plot() function, we use '.'
    # to create a scatter plot, i.e. with dots rather than lines
    plt.plot(df["species"], df["sepal_length"], ".")
    # x label
    plt.xlabel("Species")
    # y label
    plt.ylabel("Sepal Length (cm)")
    # title
    plt.title("Species vs. Sepal Length")
    # save in plots/scatterPlots folder
    plt.savefig("plots/scatterPlots/speciesSepalLength.png")
    # close the plot so that the next plot is not
    # superimposed on top of this one
    plt.close()

    plt.plot(df["species"], df["sepal_width"], ".")
    plt.xlabel("Species")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Species vs. Sepal Width")
    plt.savefig("plots/scatterPlots/speciesSepalWidth.png")
    plt.close()

    plt.plot(df["species"], df["petal_length"], ".")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.title("Species vs. Petal Length")
    plt.savefig("plots/scatterPlots/speciesPetalLength.png")
    plt.close()

    plt.plot(df["species"], df["petal_width"], ".")
    plt.xlabel("Species")
    plt.ylabel("PetalWidth (cm)")
    plt.title("Species vs. PetalWidth")
    plt.savefig("plots/scatterPlots/speciesPetalWidth.png")
    plt.close()



    # these plots plot sepal-length against the other variables in turn,
    # colouring the points according to the species
    # Sepal-length plots

    # previously I had created custom functions to slice the species-array
    # so that I could plot each species separately. However, I realised
    # afterwards that the pands groupby function can do this, and it is
    # cleaner. For the older version, see createScatterPlots2.py in the
    # filesNotUsed folder

    # groupby works here basically by working on a dataframe object and taking
    # as a parameter a column name of that dataframe. Then for every unique
    # value in that column, it creates distinct dataframe objects, so that
    # in this case, we get a dataframe object for each of the iris species.
    # It actually returns a dictionary, where the keys are the unique values
    # of the column-parameter inputted, and the values are the dataframes
    # pertaining to that particular key. This means that we can apply the
    # groupby function to the iris dataframe with 'species' inputted as a
    # parameter, and then if we iterate through this with a for loop and
    # and assign the key and value to separate variables, we can use the
    # key variable as the label for the species to be plotted and the
    # value-variable for the actual plotting of the species in question. If
    # we then include these on the same pair of axes, the species will
    # be distinguishable by colour.


    # we add a label here to distinguish between each of the species
    for label, group in df.groupby("species"):
        plt.plot(group["sepal_length"], group["sepal_width"], '.', label="setosa")

    # we add a legend to distinguish between the species, as they
    # are included on the same plot
    plt.legend()
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Sepal Length vs. Sepal Width")
    plt.savefig("plots/scatterPlots/sepalLengthSepalWidth.png")
    plt.close()

    for label, group in df.groupby("species"):
        plt.plot(group["sepal_length"], group["petal_length"], '.', label=label)

    plt.legend()
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.title("Sepal Length vs. Petal Length")
    plt.savefig("plots/scatterPlots/sepalLengthPetalLength.png")
    plt.close()

    for label, group in df.groupby("species"):
        plt.plot(group["sepal_length"], group["petal_width"], '.', label=label)

    plt.legend()
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Sepal Length vs. Petal Width")
    plt.savefig("plots/scatterPlots/sepalLengthPetalWidth.png")
    plt.close()

    # remaining sepal-width plots
    for label, group in df.groupby("species"):
        plt.plot(group["sepal_width"], group["sepal_length"], '.', label=label)


    plt.legend()
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.title("Sepal Width vs. Sepal Length")
    plt.savefig("plots/scatterPlots/sepalWidthPetalLength.png")
    plt.close()

    for label, group in df.groupby("species"):
        plt.plot(group["sepal_width"], group["petal_width"], '.', label=label)

    plt.legend()
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Sepal Width vs. Petal Width")
    plt.savefig("plots/scatterPlots/sepalWidthPetalWidth.png")
    plt.close()

    # remaining petal-length plots

    for label, group in df.groupby("species"):
        plt.plot(group["petal_length"], group["petal_width"], '.', label=label)


    plt.legend()
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Petal Length vs. Petal Width")
    plt.savefig("plots/scatterPlots/petalLengthPetalWidth.png")
    plt.close()


    # it is hard to resist using seaborn to create a matrix of
    # the above plots on a single image file
    # the following code uses the pairplot() function, where
    # the first parameter is the pandas dataframe, and the
    # second refers to the variables which are given distinct,
    # wait for it, HUES
    # for information of seaborn.pairplot, see the documentation:
    # https://seaborn.pydata.org/generated/seaborn.pairplot.html
    # and also here for a good introduction:
    # https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166
    sb.pairplot(data=df, hue="species")
    # we use matplotlit.pyplot to save the image to a file
    plt.savefig("plots/scatterPlots/scatterMatrix.png")

    # we use a raw string here to accurately depict the file path on
    # Windows systems, i.e. with '\' as the path separator.
    # see here for the use of raw string:
    # https://stackoverflow.com/questions/4415259/convert-regular-python-string-to-raw-string
    print(r"Scatter plots of the Iris dataset have have been created and saved to the 'plots\scatterPlots' directory.")


if __name__ == '__main__':
    createScatterPlots()
