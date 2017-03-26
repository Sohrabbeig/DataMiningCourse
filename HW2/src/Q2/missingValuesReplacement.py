import random

import pandas as pd
import numpy as np
import statistics as st

# load data
train = pd.read_csv("../../description/2/train.csv")
train_c = train.copy()


def valid(i):
    for m in missing:
        if isUnkown(train[m][i]):
            return True
    return False


def isUnkown(s):
    if type(s) == np.float64 and str(s) == "nan":
        return True
    return False


missing = ['LotFrontage', 'MasVnrType', 'MasVnrArea', 'Electrical', 'GarageYrBlt']
cols = list(train)
for i in range(0, train.shape[0]):
    print(i)
    if not valid(i):
        continue
    similarity = []
    minIndex = -1
    for j in range(0, train.shape[0]):
        if i == j:
            continue
        else:
            temp = 0
            for k in cols:
                if train[k][i] == train[k][j] and not (k in missing and isUnkown(train[k][j])):
                    temp += 1
            t = train.iloc[j].as_matrix()
            t = np.append(t, temp).tolist()
            if len(similarity) < 5:
                similarity.append(t)
            elif temp > similarity[minIndex][81]:
                similarity[minIndex] = t
            minIndex = np.array(similarity)[:, 81].argmin()
    for mis in missing:
        if isUnkown(train[mis][i]):
            curInd = cols.index(mis)
            try:
                train_c[mis][i] = st.mode(np.array(similarity)[:, curInd])
            except:
                train_c[mis][i] = np.array(similarity)[:, curInd][random.randint(0, 4)]
            print(train_c[mis][i])
print(train_c)
train_c.to_csv("train.csv", index=False)
