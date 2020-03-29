# get the dataframe from the createDataFrame file
from createDataFrame import df
import matplotlib.pyplot as plt
# we will use seaborn for plotting here. While pandas
# can be used for boxplots, seaborn is better.
import seaborn as sb
# there"s a very nice introduction to creating boxplots
# with seaborn here. It also demonstrates how to overlay
# over plots on top of box plots for greater clarity.
# Swarm plot is particularly effective when overlayed
# on a boxplot.

def createBoxplots():
    # because only an axes object can call the set_title method,
    # we assign the boxplot to a variable, and then use
    # that to call the set_title method
    plot = sb.boxplot(y="sepal_length", x="species", data=df, width=0.5)
    plot.set_title("Species vs. Petal Width")
    # overlay a swarm plot, specifying the color of the dots
    # as black, and making them somewhat transparent.
    plot = sb.swarmplot(y="sepal_length", x="species", data=df, color="black", alpha=0.75)
    # again, seaborn is not as user-friendly as pyplot, and
    # we must use the plot's 'figure' object to call savefig()
    plot.figure.savefig("plots/boxplots/sepalLength.png")
    # apparently, pyplot should be used to close seaborn plots:
    # https://stackoverflow.com/questions/57533954/how-to-close-seaborn-plots
    plt.close()

    plot = sb.boxplot(y="sepal_width", x="species", data=df, width=0.5)
    plot.set_title("Species vs. Sepal Width")
    plot = sb.swarmplot(y="sepal_width", x="species", data=df, color="black", alpha=0.75)
    plot.figure.savefig("plots/boxplots/sepalWidth.png")
    plt.close()

    plot = sb.boxplot(y="petal_length", x="species", data=df, width=0.5)
    plot.set_title("Species vs. Petal Length")
    plot = sb.swarmplot(y="petal_length", x="species", data=df, color="black", alpha=0.75)
    plot.figure.savefig("plots/boxplots/petalLength.png")
    plt.close()

    plot = sb.boxplot(y="petal_width", x="species", data=df, width=0.5)
    plot.set_title("Species vs. Petal Width")
    plot = sb.swarmplot(y="petal_width", x="species", data=df, color="black", alpha=0.75)
    plot.figure.savefig("plots/boxplots/petalWidth.png")
    plt.close()

    # as thee setosa petal length and width are closely clustered,
    # their boxplots are not very revealing when plotted
    # alongside the other species'. For this reason we now plot
    # them both separately.

    # we use a raw string here to accurately depict the file path on
    # Windows systems, i.e. with '\' as the path separator.
    # see here for the use of raw string:
    # https://stackoverflow.com/questions/4415259/convert-regular-python-string-to-raw-string
    print(r"Boxplots of the Iris dataset overlayed with swarm plots have have been created and saved to the 'plots\\boxPlots' directory.")

# if this is run as a script, we should call the
# createBoxplots() function, as that is what
# someone would expect to happen should they choose
# to run this rile on its own
if __name__ == '__main__':
    createBoxplots()
