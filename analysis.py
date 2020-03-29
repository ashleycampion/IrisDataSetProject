# While the other files in the repository can be run
# on their own, by running this file one can run them
# all from a central location.

from verifyIntegrityOfDataSet import verifyIntegrityOfDataSet
from createSummaryStatistics import createSummaryStatistics
from createHistograms import createHistograms
from createBoxplots import createBoxplots
from createScatterPlots import createScatterPlots


def main():
    verifyIntegrityOfDataSet()
    createSummaryStatistics()
    createHistograms()
    createBoxplots()
    createScatterPlots()


if __name__ == '__main__':
        main()
