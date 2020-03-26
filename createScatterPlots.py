import matplotlib.pyplot as plt

from createDataFrame import df
from createDataFrame import versicolor
from createDataFrame import virginica


def createScatterPlots():

    # species

    plt.plot(df["species"], df["sepal_length"], ".")
    plt.xlabel("Species")
    plt.ylabel("Sepal Length (cm)")
    plt.title("Species vs. Sepal Length")
    plt.savefig("plots/scatterPlots/speciesSepalLength.png")
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

    # Sepal length
    plt.scatter(df["sepal_length"][:versicolor], df["sepal_width"][:versicolor], s=20, label="setosa")
    plt.scatter(df["sepal_length"][versicolor:virginica], df["sepal_width"][versicolor:virginica], s=20, label="versicolor")
    plt.scatter(df["sepal_length"][virginica:], df["sepal_width"][virginica:], s=20, label="virginica")

    plt.legend()
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Sepal Length vs. Sepal Width")
    plt.savefig("plots/scatterPlots/sepalLengthSepalWidth.png")
    plt.close()

    plt.scatter(df["sepal_length"][:versicolor], df["petal_length"][:versicolor], s=20, label="setosa")
    plt.scatter(df["sepal_length"][versicolor:virginica], df["petal_length"][versicolor:virginica], s=20, label="versicolor")
    plt.scatter(df["sepal_length"][virginica:], df["petal_length"][virginica:], s=20, label="virginica")

    plt.legend()
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.title("Sepal Length vs. Petal Length")
    plt.savefig("plots/scatterPlots/sepalLengthPetalLength.png")
    plt.close()

    plt.scatter(df["sepal_length"][:versicolor], df["petal_width"][:versicolor], s=20, label="setosa")
    plt.scatter(df["sepal_length"][versicolor:virginica], df["petal_width"][versicolor:virginica], s=20, label="versicolor")
    plt.scatter(df["sepal_length"][virginica:], df["petal_width"][virginica:], s=20, label="virginica")

    plt.legend()
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Sepal Length vs. Petal Width")
    plt.savefig("plots/scatterPlots/sepalLengthPetalWidth.png")
    plt.close()

    # Sepal width
    plt.scatter(df["sepal_width"][:versicolor], df["petal_length"][:versicolor], s=20, label="setosa")
    plt.scatter(df["sepal_width"][versicolor:virginica], df["petal_length"][versicolor:virginica], s=20, label="versicolor")
    plt.scatter(df["sepal_width"][virginica:], df["petal_length"][virginica:], s=20, label="virginica")

    plt.legend()
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.title("Sepal Width vs. Sepal Length")
    plt.savefig("plots/scatterPlots/sepalWidthPetalLength.png")
    plt.close()

    plt.scatter(df["sepal_width"][:versicolor], df["petal_width"][:versicolor], s=20, label="setosa")
    plt.scatter(df["sepal_width"][versicolor:virginica], df["petal_width"][versicolor:virginica], s=20, label="versicolor")
    plt.scatter(df["sepal_width"][virginica:], df["petal_width"][virginica:], s=20, label="virginica")

    plt.legend()
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Sepal Width vs. Petal Width")
    plt.savefig("plots/scatterPlots/sepalWidthPetalWidth.png")
    plt.close()

    # Petal length

    plt.scatter(df["petal_length"][:versicolor], df["petal_width"][:versicolor], s=20, label="setosa")
    plt.scatter(df["petal_length"][versicolor:virginica], df["petal_width"][versicolor:virginica], s=20, label="versicolor")
    plt.scatter(df["petal_length"][virginica:], df["petal_width"][virginica:], s=20, label="virginica")


    plt.legend()
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Petal Length vs. Petal Width")
    plt.savefig("plots/scatterPlots/petalLengthPetalWidth.png")
    plt.close()
