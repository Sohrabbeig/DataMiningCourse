from sklearn import ensemble
from sklearn.metrics import mean_squared_error
import pandas as pd
import math
import numpy as np
from sklearn.model_selection import KFold

train = pd.read_csv("../train.csv", header=None, names=['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'])
# del train['G0']
t = np.asarray(train)

params = {'n_estimators': 500, 'max_depth': 3, 'min_samples_split': 2,
          'learning_rate': 0.005, 'loss': 'ls'}

kf = KFold(n_splits=10)
RMSE = 0
for tr, te in kf.split(t):
    xtr = []
    ytr = []
    xte = []
    yte = []
    for i in tr:
        xtr.append(t[i, [0, 1, 2, 3, 4, 5]])
        ytr.append(t[i, [6]])
    clf = ensemble.GradientBoostingRegressor(**params)
    clf.fit(np.asarray(xtr), np.asarray(ytr))
    for j in te:
        xte.append(t[j, [0, 1, 2, 3, 4, 5]])
        yte.append(t[j, [6]])
    mse = mean_squared_error(np.asarray(yte), clf.predict(np.asarray(xte)))
    RMSE += math.sqrt(mse)
RMSE /= 10
print(RMSE)
