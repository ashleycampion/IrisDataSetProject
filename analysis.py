# While the other files in the repository can be run
# on their own, by running this file one can run them
# all from a central location.

from verifyIntegrityOfDataSet import verifyIntegrityOfDataSet
from createSummaries import createSummaries
from createHistograms import createHistograms
from createScatterPlots import createScatterPlots


def main():
    verifyIntegrityOfDataSet()
    createSummaries()
    createHistograms()
    createScatterPlots()


if __name__ == '__main__':
        main()
