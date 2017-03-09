# Create train_two
train_two <- train
train_two$family_size <- train_two$SibSp + train_two$Parch + 1

test_two <- test
test_two$family_size <- test_two$SibSp + test_two$Parch + 1

# Finish the command
my_tree_four <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked + family_size,
                      data = train_two, method = "class")

# Visualize your new decision tree
fancyRpartPlot(my_tree_four)

# Make predictions on the test set
my_prediction <- predict(my_tree_four, test_two, type = "class")

# Finish the data.frame() call
my_solution <- data.frame(PassengerId = test$PassengerId, Survived = my_prediction)

# Use nrow() on my_solution
nrow(my_solution)

# Finish the write.csv() call
write.csv(my_solution, file = "6th_prediction.csv", row.names = FALSE)