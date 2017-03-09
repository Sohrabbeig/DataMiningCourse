# Import the training set: train
train_url <- "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train <- read.csv(train_url)

# Create the column child, and indicate whether child or no child
train$Child <- NA
train$Child[train$Age < 18] <- 1
train$Child[train$Age >= 18] <- 0

# Two-way comparison
prop.table(table(train$Child,train$Survived),1)

# Import the testing set: test
test_url <- "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test <- read.csv(test_url)

PassengerId <- as.vector(test$PassengerId)
test_one <- data.frame(PassengerId)
test_one$Survived <- 0
test_one$Survived[test$Age < 18] <- 1 
write.csv(test_one, file = "third_prediction.csv",row.names=FALSE)
