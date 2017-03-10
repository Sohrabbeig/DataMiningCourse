import pandas as pd
import numpy as np
from numpy.linalg import inv

# load data
train = pd.read_csv("../../description/1/train.csv", header=None, names=['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'])
train.insert(0, 'G0', 1)
test = pd.read_csv("../../description/1/test.csv", header=None, names=['G1', 'G2', 'G3', 'G4', 'G5', 'G6'])
test.insert(0, 'G0', 1)


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
train_c = train_c.astype(int)
train_c.to_csv("train.csv", index=False, header=False)


def f4(i2):
    x2 = test[test[i2] != 0]
    y2 = x2[i2]
    del x2[i2]
    return x2, y2


def f5(j2):
    col2 = list(xTest)[j2]
    xTemp2 = xTest[['G0', col2]][xTest[col2] != 0].as_matrix()
    yTemp2 = yTest[xTest[col2] != 0].as_matrix()
    trans2 = xTemp2.transpose()
    t2 = np.dot(np.dot(inv(np.dot(trans2, xTemp2)), trans2), yTemp2)
    return t2


def f6(m2):
    temp2 = 0
    iteration2 = 0
    for k2 in mylist2:
        if train[k2][m2] != 0:
            temp2 += theta[k2][0] + theta[k2][1] * test[k2][m2]
            iteration2 += 1
    return temp2 / iteration2


mylist2 = list(test)[1:7]
test_c = test.copy()
for i2 in mylist2:  # replacing missing values for each column
    xTest, yTest = f4(i2)
    theta2 = {}
    testIndex = set(yTest.index.values)
    mainIndex2 = set(test.index.values)
    index2 = mainIndex2.difference(testIndex)
    for j2 in range(1, xTest.shape[1]):
        theta2[list(xTest)[j2]] = f5(j2)

    for m2 in index2:
        test_c[i2][m2] = f6(m2)

print(test_c)
test_c = test_c.astype(int)
test_c.to_csv("test.csv", index=False, header=False)
