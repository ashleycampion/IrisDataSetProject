# Programming and Scripting Project
# Analysis of Fisher's Iris Dataset

## Table of Contents
1. [Housekeeping](#housekeeping)
    * [Python Files in this Repository](#files-in-this-repository)
    * [How to Download this Repository](#how-to-download-this-repository)
    * [What is Needed to Run the Python Scripts](#what-is-needed-to-run-the-python-scripts)
    * [How to Run the Python Scripts](#how-to-run-the-python-scripts)
1. [Introduction to the Dataset](#introduction-to-the-dataset)
    * [What is the Iris Dataset?](#what-is-the-iris-dataset?)
    * [Why is the Iris Dataset Still Relevant?](#why-is-the-iris-dataset-still-relevant?)
1. [Analysis of the Dataset](#analysis-of-the-data-set)
    * [Conceptualizing the Dataset](#conceptualizing-the-data-set)
    * [Histograms](#histograms)
    * [Box Plots](#box-plots)
    * [Scatter Plots](#scatter-plots)
    * [Parallel Coordinates Plots](#parallel-coordinates-plot)
    * [Linear Regression](#linear-regression)
1. [Appendix](#appendix)
    * [Definitions of Key Terms](#definition-of-key-terms)
1. [References](#references)

# Housekeeping

## Python Files in this Repository
* an 'analysis' file which is the main application script and which imports and runs the functions in the other files
* a 'createBoxplots' file that saves boxplots overlayed with swarm plots to the plots\boxplots folder
* a 'createDataFrame' file that creates a pandas dataframe object based on the irisDataSet file
* a 'createHistograms' file that saves histograms for to the plots\histograms folder
* a 'createParallelCoordinates' file that saves a parallel coordinates plot to the plots\parallelCoordinates folder
* a 'createScatterPlots' file that saves scatter plots to the plots\scatterPlots folder
* a 'createSummaryStatistics' file that saves summary statistics for each species to a csv file in the summaryStatistics folder
* a 'verifyIntegrityOfDataset' file to do just that

## How to Download this Repository
Click on the green 'Clone or download' button near the top right of this page, and then select 'Download ZIP'. You will then need to unzip the downloaded file. You can download 7-zip [here](https://www.7-zip.org/download.html).

## What is Needed to Run the Python Scripts
Python 3.7.4 was used to create the scripts in this repository (download it [here](https://www.python.org/downloads/)). Detailed instructions on how to download and install the latest version of Python are available [here](https://realpython.com/installing-python/). Any version of Python 3 can run the scripts. You can also download Python by downloading the Python distribution, Anaconda. You can download Anaconda [here](https://www.anaconda.com/distribution/), and you will find instructions on how to download and install Anaconda for Windows [here](https://docs.anaconda.com/anaconda/install/windows/).

## How to Run the Python Scripts
See the section 'How to Run Python Scripts Using the Command-Line' [here](https://realpython.com/run-python-scripts/).


# Introduction to the Dataset

## What is the Iris Dataset

From Wikipedia:
> The Iris flower data set or Fisher's Iris data set is a [multivariate](#multivariate) (these blue links will take you to a definition in the appendix section below) data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems as an example of [linear discriminant analysis](#linear-indiscriminate-analysis).
> The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. [1]


## Why is the Iris Dataset Still Relevant?


# **Analysis of the Dataset**

## Conceptualizing the Dataset
## Histograms
## Box Plots
## Scatter Plots
## Parallel Coordinates
## Linear Regression



# Appendix

## Definition of Key Terms

<dl>
    <dt><a id='Linear Combination'></a>Linear Combination</dt>
    <dd>In mathematics, a linear combination is an expression constructed from a set of terms by multiplying each term by a constant and adding the results (e.g. a linear combination of x and y would be any expression of the form ax + by, where a and b are constants) [4].</dd>
    <dt><a id='Linear Discriminate Analysis'></a>Linear Discriminate Analysis</dt>
    <dd>Linear discriminant analysis (LDA), normal discriminant analysis (NDA), or discriminant function analysis is a generalization of Fisher's linear discriminant, a method used in statistics, pattern recognition, and machine learning to find a <a href="#linear combination">linear combination</a> of features that characterizes or separates two or more classes of objects or events [3].</dd>
    <dt><a id='Multivariate'>Multivariate</a></dt>
    <dd>Multivariant refers to the property of having multiple variables. Hence a <em>multivariate dataset</em> is a dataset with multiple variables, and <em>multivariate statistics</em> is the statistics of multivariate datasets.</dd>
    <dt></dt>
    <dd></dd>
    <dt></dt>
    <dd></dd>
    <dt></dt>
    <dd></dd>
    <dt></dt>
    <dd></dd>
    <dt></dt>
    <dd></dd>
</dl>

# References
1 https://en.wikipedia.org/wiki/Iris_flower_data_set
2 https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
3 https://en.wikipedia.org/wiki/Linear_discriminant_analysis
4 https://en.wikipedia.org/wiki/Linear_combination
