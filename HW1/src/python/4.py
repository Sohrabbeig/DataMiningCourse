import pandas as pd
import numpy as np

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

# Initialize a Survived column to 0
test["Survived"] = 0

# Set Survived to 1 if age is less than 18 and to 0 if age in greater equal than 18
test["Survived"][test["Age"] < 18] = 1
test["Survived"][test["Age"] >= 18] = 0

PassengerId =np.array(test["PassengerId"]).astype(int)
my_solution = pd.DataFrame(test[["Survived"]].as_matrix(), PassengerId, columns = ["Survived"])
my_solution.to_csv("my_solution_three.csv", index_label = ['PassengerId'])