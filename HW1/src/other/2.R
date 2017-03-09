# Import the training set: train
train_url <- "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train <- read.csv(train_url)

# Import the testing set: test
test_url <- "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test <- read.csv(test_url)

PassengerId <- as.vector(test$PassengerId)
test_one <- data.frame(PassengerId)
test_one$Survived <- 0
write.csv(test_one, file = "first_prediction.csv",row.names=FALSE)
