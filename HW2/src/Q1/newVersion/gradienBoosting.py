from sklearn import ensemble
from sklearn.metrics import mean_squared_error
import pandas as pd
import math

train = pd.read_csv("../train.csv", header=None, names=['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'])
test = pd.read_csv("../test.csv", header=None, names=['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6'])

yTrain = train['G7'].as_matrix()
del train['G7']
xTrain = train.as_matrix()

params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,
          'learning_rate': 0.01, 'loss': 'ls'}
clf = ensemble.GradientBoostingRegressor(**params)

clf.fit(xTrain, yTrain)
mse = mean_squared_error(yTrain, clf.predict(xTrain))
print("RMSE: %.4f" % math.sqrt(mse))
