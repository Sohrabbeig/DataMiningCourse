import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor


# regressor = RandomForestRegressor(n_estimators=150, min_samples_split=1)
# regressor.fit(X, y)
# print(regressor.predict(X))

import pandas as pd

# load data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

y = train['SalePrice'].as_matrix()
del train['SalePrice']
x = train.as_matrix()
z = test.as_matrix()
temp = 1461
for i in x[:, 25]:
    if type(i) != str:
        print(temp)
    temp += 1
# transform 1st column to numbers
# for i in range(0, 80):
#     if not isinstance(x[0][i], (int, float)):
#         print(x[0][i])
#         x[:, i] = LabelEncoder().fit_transform(x[:, i])
#
# regressor = RandomForestRegressor(n_estimators=150, min_samples_split=1)
# regressor.fit(x, y)
# prediction = regressor.predict(z)
# print(type(prediction))
