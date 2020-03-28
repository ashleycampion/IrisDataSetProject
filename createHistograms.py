# an older version of this file can be found in the filesNotUsed
# folder, createHistograms1.py

# we want numpy for creating numpy arrays with linspace
# method. Linspace can easily create arrays with steps
# of floating point magnitudes, which will be helpful
# for specifying the bins for the histograms.
import numpy as np
# for creating the actual histograms we want matplotlib.pyplot
import matplotlib.pyplot as plt
# get the dataframe from the createDataFrame file
from createDataFrame import df

# interestingly, we don't actually need to import pandas here
# because we will by using the dataframe imported above to
# call the groupby function of pandas

# this function will be called by the main analysis file
def createHistograms():

    # originally I created histograms for all of the variables.
    # However, as histograms only plot one variable, they are
    # really only useful when compared against each other.
    # Thus, I instead created one images with histograms for
    # each of the variables regardless of species. Next I created
    # plots for the variables (this time saved to separate images),
    # and plotted the variables separately for each species, but
    # including each of the three plots for each variable on the same
    # axis. This allows differences between the species to be more
    # easily compared. Finally I incorporated all of the four plots
    # created in the last step into a single image, for even more
    # comprehensive comparison.

    # to incorporate multiple axes on the one image, use the subplot
    # method, the first paramater defines the number of axes
    # vertically, the next horizontally, and the third parameter
    # defines what axes will be plotted next, where '1' refers to the
    # top left axis, '2' refers to the axis to the right of '1' (or below
    # if there is no plot to the right) and on the last axis.
    # see the documentation here:
    # https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.subplot.html

    # In the case of creating histograms for each of the
    # variables independent of species, I decided not to vary
    #  the bins across the histograms. While this is not
    # ideal in the sense that there will be a lot of "white
    # space" on some of the histograms, I think this is made up for
    # by the ease with which one can compare the histograms, i.e. one
    # does not have to factor in the range of the bins but can compare
    # the variables and species purely by looking at the plots.
    # 8 is the upper bound (virginica sepal length) and 0 is the lower
    # (setosa petal width). While bins of 0.25 width are probably the
    # most visually appealing, the setosa-petal values are clumped
    # together so much that histograms with a width of 0.5 really aren"t
    # granular enough. Bins of 0.125 have been used instead.

    plt.subplot(2,2,1)
    plt.hist(df["sepal_length"], bins=np.linspace(0,8,64))
    # we don"t want to label the x axis here, as it would
    # overlap with the plot under it
    # plt.xlabel("Length (cm)")
    # include the label for the y axis
    plt.ylabel("Occurences")
    # we want the xticks and yticks to be the same across
    # all the subplots. The xticks will be the same because
    # the bins are the same, the yticks need to be explicitly
    # defined. We don"t want things to get too messy, so ticks
    # of 0, 10 and 20 should suffice.
    plt.yticks([0,10,20])

    # give the plot its title
    plt.grid()
    plt.title("Overall Sepal Length")

    # as we are creating subplots all on the one file, we do not
    # save it yet, nor close the plot

    plt.subplot(2,2,2)
    plt.hist(df["sepal_width"], bins=np.linspace(0,8,64))
    # we don"t either of the labels here, and they would overlap with
    # the other plots" axes anyway
    # plt.xlabel("Width (cm)")
    # plt.ylabel("Occurences")
    plt.yticks([0,10,20])
    plt.grid()
    plt.title("Overall Sepal Width")

    plt.subplot(2,2,3)
    plt.hist(df["petal_length"], bins=np.linspace(0,8,64))
    plt.xlabel("Length (cm)")
    plt.ylabel("Occurences")
    plt.yticks([0,10,20])
    plt.grid()
    plt.title("Overall Petal Length")

    plt.subplot(2,2,4)
    plt.hist(df["petal_width"], bins=np.linspace(0,8,64))
    plt.xlabel("Width (cm)")
    # plt.ylabel("Occurences")
    plt.yticks([0,10,20])
    plt.grid()
    plt.title("Overall Petal Width")

    # To avoid the titles of the bottom plots and the x axis labels
    # of the upper plots from overlapping.
    plt.tight_layout()
    # save it to a file in the plots/histogram folder
    plt.savefig("plots/histograms/allSpeciesHistograms.png")
    # and close the plot so that the next plot is not
    # superimposed on top of this one
    plt.close()


    # when plotting multiple plots on the same axes, the easiest
    # way is to use the groupby function in pandas. The use of this
    # is explained in more detail in the createScatterPlots.py file.
    # Here, it basically allows us to create separate histograms
    # for each of the species, and then show them on the same
    # axes. Because we have a lot of data on each axis now,
    # we want to make the legend semi-transpart with the
    # alphaframe keyword argument, and the plots themselves
    # semi-transparent with the alpha keword argument of the
    # hist function. Because we are concerned here with comparing
    # the species against each other on the same axes, there is less
    # need to have the xticks and yticks and bins the same across
    # all axes, so we can just not specify the ticks and have 10
    # bins for each plot.
    # for alphaframe keyword argument of legend() see here:
    # https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.legend.html
    # for alpha see here:
    # http://www.learningaboutelectronics.com/Articles/How-to-change-the-transparency-of-a-graph-plot-in-matplotlib-with-Python.php

    # one can actually call the hist() method with the result of a groupby() call,
    # assign the list of values grouped by to the labels keyword argument,
    # and the hist will create plots for each of the groups! This
    # doesn't seem possible with the plot() method, perhaps because
    # plot() requires two arguments, and so one would have to both
    # call the plot() method with one groupby() result, and then include
    # another groupby() result as the first parameter to the plot() method,
    # which doesn't intuitively make sense.

    # to get a list of the species, we can call the unique() method
    # on the array-like object df.species. For more on unique() see:
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.unique.html
    labels = df.species.unique()

    # Sepal Length for each species
    df.groupby("species")["sepal_length"].hist(bins=10, alpha=0.5, label=labels)
    plt.title("Sepal Length")
    plt.xlabel("Length (cm)")
    plt.ylabel("Occurences")
    plt.legend()
    plt.savefig("plots/histograms/sepalLength.png")
    plt.close()

    # Sepal Width for each species
    df.groupby("species")["sepal_width"].hist(bins=10, alpha=0.5, label=labels)
    plt.title("Sepal Width")
    plt.xlabel("Width (cm)")
    plt.ylabel("Occurences")
    plt.legend()
    plt.savefig("plots/histograms/sepalWidth.png")
    plt.close()

    # Petal Length for each species
    df.groupby("species")["petal_length"].hist(bins=10, alpha=0.5, label=labels)
    plt.title("Petal Length")
    plt.xlabel("Length (cm)")
    plt.ylabel("Occurences")
    plt.legend()
    plt.savefig("plots/histograms/petalLength.png")
    plt.close()

    # Petal Width for each species
    df.groupby("species")["petal_width"].hist(bins=10, alpha=0.5, label=labels)
    plt.title("Petal Width")
    plt.xlabel("Width (cm)")
    plt.ylabel("Occurences")
    plt.legend()
    plt.savefig("plots/histograms/petalWidth.png")
    plt.close()

    plt.subplot(2,2,1)
    df.groupby("species")["sepal_length"].hist(bins=10, alpha=0.5, label=labels)
    plt.title("SepalLength")
    #plt.xlabel("Length (cm)")
    plt.ylabel("Occurences")
    plt.legend(framealpha=0.5)

    plt.subplot(2,2,2)
    df.groupby("species")["sepal_width"].hist(bins=10, alpha=0.5, label=labels)
    plt.title("SepalWidth")
    #plt.xlabel("Width (cm)")
    #plt.ylabel("Occurences")
    plt.legend(framealpha=0.5)

    plt.subplot(2,2,3)
    df.groupby("species")["petal_length"].hist(bins=10, alpha=0.5, label=labels)
    plt.title("PetalLength")
    plt.xlabel("Length (cm)")
    plt.ylabel("Occurences")
    plt.legend(framealpha=0.5)

    plt.subplot(2,2,4)
    df.groupby("species")["petal_width"].hist(bins=10, alpha=0.5, label=labels)
    plt.title("PetalWidth")
    plt.xlabel("Width (cm)")
    #plt.ylabel("Occurences")
    plt.legend(framealpha=0.5)

    plt.tight_layout()

    plt.savefig("plots/histograms/overallHistograms.png")
    plt.close()



# if this is run as a script, we should call the
# createHistograms() function, as that is what
# someone would expect to happen should they choose
# to run this rile on its own
if __name__ == '__main__':
    createHistograms()
