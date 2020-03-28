import pandas as pandas
from createDataFrame import df


    def createSummaryStatistics():
    # see here for an explanation of 'loc':
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
    setosaSummary = df.loc[df['species'] == "setosa"].describe()
    versicolorSummary = df.loc[df['species'] == "versicolor"].describe()
    virginicaSummary = df.loc[df['species'] == "virginica"].describe()

    setosaSummary.to_csv("summaryStatistics/setosaSummaryStats.csv")
    versicolorSummary.to_csv("summaryStatistics/versicolorSummaryStats.csv")
    virginicaSummary.to_csv("summaryStatistics/virgnicaSummaryStats.csv")

    print("Summary statistics for each species have been written to csv files in the summaryStatistics folder.")




if __name__ == '__main__':
    createSummaryStatistics()
