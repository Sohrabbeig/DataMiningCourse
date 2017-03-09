# Import the testing set: test
test_url <- "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test <- read.csv(test_url)

PassengerId <- as.vector(test$PassengerId)
test_one <- data.frame(PassengerId)
test_one$Survived <- 0
test_one$Survived[test$Sex == "female"] <- 1 
write.csv(test_one, file = "second_prediction.csv",row.names=FALSE)

