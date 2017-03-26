import pandas as pd
import numpy as np
import statistics as st

# load data
# train = pd.read_csv("train.csv")
# test = pd.read_csv("../../description/2/test.csv")
# test_c = test.copy()
# test_c['SalePrice'] = 0
#
# cols = list(test)
# for i in range(0, test.shape[0]):
#     print(i)
#     similarity = []
#     minIndex = -1
#     for j in range(0, train.shape[0]):
#         temp = 0
#         for k in cols:
#             if test[k][i] == train[k][j]:
#                 temp += 1
#         t = train.iloc[j].as_matrix()
#         t = np.append(t, temp).tolist()
#         if len(similarity) < 5:
#             similarity.append(t)
#         elif temp > similarity[minIndex][81]:
#             similarity[minIndex] = t
#         minIndex = np.array(similarity)[:, 81].argmin()
#     test_c['SalePrice'][i] = st.mean(list(map(int, np.array(similarity)[:, 80])))
# print(test_c)
# test_c.to_csv("test.csv", index=False)

test = pd.read_csv("test.csv")
Id = np.array(test["Id"]).astype(int)
my_solution = pd.DataFrame(test[["SalePrice"]].as_matrix(), Id, columns = ["SalePrice"])
my_solution.to_csv("submission.csv", index_label=['Id'])
