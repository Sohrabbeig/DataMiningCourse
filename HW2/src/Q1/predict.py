import pandas as pd
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr

# load data
train = pd.read_csv("train.csv", header=None, names=['G0','G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'])
test = pd.read_csv("test.csv", header=None, names=['G0','G1', 'G2', 'G3', 'G4', 'G5', 'G6'])
yTrain = train['G7'].as_matrix()[1:].astype(int)
del train['G7']
xTrain = train.as_matrix()[1:].astype(int)
xTest = test.as_matrix().astype(int)
trans = xTrain.transpose()
theta = np.dot(np.dot(inv(np.dot(trans, xTrain)), trans), yTrain)
grades = np.dot(xTest,theta)
del test['G0']
test['G7'] = grades
test.to_csv("test.csv", index=False)

