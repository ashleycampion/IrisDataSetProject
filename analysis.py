# While the other files in the repository can be run
# on their own, by running this file one can run them
# all from a central location.

from verifyIntegrityOfDataSet import verifyIntegrityOfDataSet
from createSummaryStatistics import createSummaryStatistics
from createHistograms import createHistograms
from createBoxPlots import createBoxPlots
from createScatterPlots import createScatterPlots
from dimensionalityReduction import createLDAScatterPlot
from dimensionalityReduction import homemadeDimensionalityReduction


def main():
    verifyIntegrityOfDataSet()
    createSummaryStatistics()
    createHistograms()
    createBoxPlots()
    createScatterPlots()
    createLDAScatterPlot()
    homemadeDimensionalityReduction()

if __name__ == '__main__':
        main()
