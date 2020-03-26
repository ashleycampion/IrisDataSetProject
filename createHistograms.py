import matplotlib.pyplot as plt

from createDataFrame import df

def createHistograms():

    plt.hist(df["sepal_length"], bins=[4,4.25,4.5,4.75,5,5.25,5.5,5.75,6,6.25,6.5,6.75,7,7.25,7.5,7.75,8])
    plt.xlabel("Sepal Length")
    plt.ylabel("Occurences")
    plt.title("Sepal Length")
    plt.savefig("plots/sepalLength.png")
    plt.close()

    plt.hist(df["sepal_width"], bins=[2,2.25,2.5,2.75,3,3.25,3.5,3.75,4,4.25,4.5])
    plt.xlabel("Sepal Width")
    plt.ylabel("Occurences")
    plt.title("Sepal Width")
    plt.savefig("plots/sepalWidth.png")
    plt.close()

    plt.hist(df["petal_length"], bins=[1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7])
    plt.xlabel("Petal Length")
    plt.ylabel("Occurences")
    plt.title("Petal Length")
    plt.savefig("plots/petalLength.png")
    plt.close()

    plt.hist(df["petal_width"], bins=[0,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5])
    plt.xlabel("Petal Width")
    plt.ylabel("Occurences")
    plt.title("Petal Width")
    plt.savefig("plots/petalWidth.png")
    plt.close()
