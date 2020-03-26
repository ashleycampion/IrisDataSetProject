import pandas as pd

df = pd.read_csv("irisDataSet.txt")

versicolor = 0
virginica = 0

def findIndexesForSlicing(df):
    global versicolor
    global virginica
    for i in range(len(df)):
        if df[i] =='versicolor':
            versicolor = i
            break
    for i in range(len(df)):
        if df[i] == 'virginica':
            virginica = i
            break

findIndexesForSlicing(df["species"])
