import pandas as pd
import numpy as np
from numpy.linalg import inv

# load data
train = pd.read_csv("../../description/1/train.csv", header=None, names=['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'])
train.insert(0, 'G0', 1)
test = pd.read_csv("../../description/1/test.csv", header=None, names=['G1', 'G2', 'G3', 'G4', 'G5', 'G6'])
test.insert(0, 'G0', 1)


def decompose_training_set(i):
    x = train[train[i] != 0]
    y = x[i]
    del x[i]
    return x, y


def calculate_theta(j):   # calculates theta for j th feature
    xTemp = xTrain[['G0', j]][xTrain[j] != 0].as_matrix()
    yTemp = yTrain[xTrain[j] != 0].as_matrix()
    trans = xTemp.transpose()
    t = np.dot(np.dot(inv(np.dot(trans, xTemp)), trans), yTemp)
    return t


def fill_missing_values(m):   # filling missing values using theta array
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
    xTrain, yTrain = decompose_training_set(i)
    theta = {}
    trainIndex = set(yTrain.index.values)  # indices of non zero records
    mainIndex = set(train.index.values)  # indices of the whole set
    index = mainIndex.difference(trainIndex)   # indices of zero value records

    for j in list(xTrain)[1:]:
        theta[j] = calculate_theta(j)

    for m in index:
        train_c[i][m] = fill_missing_values(m)

print(train_c)
train_c = train_c.astype(int)
train_c.to_csv("train.csv", index=False, header=False)


def decompose_test_set(i):
    x = test[test[i] != 0]
    y = x[i]
    del x[i]
    return x, y


def calculate_theta2(j):  # calculates theta for j th feature
    xTemp = xTest[['G0', j]][xTest[j] != 0].as_matrix()
    yTemp = yTest[xTest[j] != 0].as_matrix()
    trans = xTemp.transpose()
    t = np.dot(np.dot(inv(np.dot(trans, xTemp)), trans), yTemp)
    return t


def fill_missing_values2(m):  # filling missing values using theta2 array
    temp = 0
    iteration = 0
    for k in mylist2:
        if test[k][m] != 0:
            temp += theta2[k][0] + theta2[k][1] * test[k][m]
            iteration += 1
    return temp / iteration


mylist2 = list(test)[1:7]
test_c = test.copy()
for i in mylist2:  # replacing missing values for each column
    xTest, yTest = decompose_test_set(i)
    theta2 = {}
    testIndex = set(yTest.index.values)  # indices of non zero records
    mainIndex2 = set(test.index.values)  # indices of the whole set
    index2 = mainIndex2.difference(testIndex)  # indices of zero value records

    for j in list(xTest)[1:]:
        theta2[j] = calculate_theta2(j)

    for m in index2:
        test_c[i][m] = fill_missing_values2(m)

print(test_c)
test_c = test_c.astype(int)
test_c.to_csv("test.csv", index=False, header=False)
