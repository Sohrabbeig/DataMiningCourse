import pandas as pd
import numpy as np
from numpy.linalg import inv

# load data
train = pd.read_csv("../../description/1/train.csv", header=None, names=['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'])
train.insert(0, 'G0', 1)

def f1(i):
    x = train[train[i] != 0]
    y = x[i]
    del x[i]
    return x, y


def f2(j):
    col = list(xTrain)[j]
    xTemp = xTrain[['G0', col]][xTrain[col] != 0].as_matrix()
    yTemp = yTrain[xTrain[col] != 0].as_matrix()
    trans = xTemp.transpose()
    t = np.dot(np.dot(inv(np.dot(trans, xTemp)), trans), yTemp)
    return t


def f3(m):
    temp = 0
    iteration = 0
    for k in mylist:
        if train[k][m] != 0:
            temp += theta[k][0] + theta[k][1] * train[k][m]
            iteration += 1
    return temp / iteration


mylist = list(train)[1:8]
train_c = train.copy()
for i in mylist:  # replacing missing values for each column
    xTrain, yTrain = f1(i)
    theta = {}
    trainIndex = set(yTrain.index.values)
    mainIndex = set(train.index.values)
    index = mainIndex.difference(trainIndex)
    for j in range(1, xTrain.shape[1]):
        theta[list(xTrain)[j]] = f2(j)

    for m in index:
        train_c[i][m] = f3(m)

print(train_c)

