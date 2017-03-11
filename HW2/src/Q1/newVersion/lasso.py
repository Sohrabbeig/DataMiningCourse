from sklearn import linear_model
import pandas as pd
import numpy as np
import math

train = pd.read_csv("../train.csv", header=None, names=['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'])
test = pd.read_csv("../test.csv", header=None, names=['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6'])

reg = linear_model.Lasso(alpha=0.1)

yTrain = train['G7'].as_matrix()
del train['G7']
xTrain = train.as_matrix()

reg.fit(xTrain, yTrain)

# The coefficients
print('Coefficients: \n', reg.coef_)

# The mean squared error
print("RootMean squared error: %.2f"
      % math.sqrt(np.mean((reg.predict(xTrain) - yTrain) ** 2)))
