# Import the training set: train
train_url <- "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train <- read.csv(train_url)

# Import the testing set: test
test_url <- "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test <- read.csv(test_url)

# Print train and test to the console
str(test)
str(train)

# Survival rates in absolute numbers
print(table(train$Survived)) 

# Survival rates in proportions
print(prop.table(table(train$Survived)))

# Two-way comparison: Sex and Survived
print(table(train$Sex, train$Survived))

# Two-way comparison: row-wise proportions
print(prop.table(table(train$Sex, train$Survived), margin = 1))