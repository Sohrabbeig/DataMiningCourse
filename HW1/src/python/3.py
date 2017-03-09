import pandas as pd
import numpy as np

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

# Initialize a Survived column to 0
test["Survived"] = 0

# Set Survived to 1 if Sex equals "female" and print the `Survived` column from `test_one`
test["Survived"][test["Sex"] == "female"] = 1

PassengerId =np.array(test["PassengerId"]).astype(int)
my_solution = pd.DataFrame(test[["Survived"]].as_matrix(), PassengerId, columns = ["Survived"])
my_solution.to_csv("my_solution_two.csv", index_label = ['PassengerId'])