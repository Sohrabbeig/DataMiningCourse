# Import the Pandas library
import pandas as pd

# Load the train and test datasets to create two DataFrames
train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

# Passengers that survived vs passengers that passed away
print("Passengers that survived vs passengers that passed away")
print(train["Survived"].value_counts())
print("------------------------")

# As proportions
print("Passengers that survived vs passengers that passed away as proportion")
print(train["Survived"].value_counts(normalize = True))
print("------------------------")

# Males that survived vs males that passed away
print("Males that survived vs males that passed away")
print(train["Survived"][train["Sex"] == 'male'].value_counts())
print("------------------------")

# Females that survived vs Females that passed away
print("Females that survived vs Females that passed away")
print(train["Survived"][train["Sex"] == 'female'].value_counts())
print("------------------------")

# Normalized male survival
print("Normalized male survival")
print(train["Survived"][train["Sex"] == 'male'].value_counts(normalize = True))
print("------------------------")

# Normalized female survival
print("Normalized female survival")
print(train["Survived"][train["Sex"] == 'female'].value_counts(normalize = True))
print("------------------------")