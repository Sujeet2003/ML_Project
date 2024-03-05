Linear Regression using Python
Let’s consider a simple example of a Machine Learning method: Linear Regression. This is a basic predictive analytics technique. It’s used when the target (the variable we want to predict) is continuous.

Create linear regression object: A linear regression model is created using sklearn.
Train the model: The model is trained using the training data (X_train and y_train).
Make predictions: The trained model is used to make predictions on the test data (X_test). The predicted values are stored in y_pred.
Compare actual output values for X_test with the predicted values: A new DataFrame is created that shows the actual values from the test set (y_test) and the predicted values (y_pred). This is printed out to give a comparison of the model’s predictions with the actual values.

Actual: These are the true values for the target variable, which in this case seems to be “Got Marks”. These are the actual marks that were observed in the dataset.
Predicted: These are the values that the linear regression model predicted for the target variable (“Got Marks”) based on the input feature(s) (“Study Hours”).

The goal is to predict “Got Marks” based on “Study Hours”. This could represent, for example, a dataset of students where “Study Hours” is the number of hours a student studied and “Got Marks” is the score they received on a test. The model is then used to predict a student’s score based on how many hours they studied.

regressor.fit(X_train, y_train): This line is where the model is actually being trained. The fit method takes the training data and learns the coefficients of the linear regression equation.
X_train and y_train are passed to the fit method. The model learns the relationship between the features (X_train) and the target variable (y_train).
The learning process involves finding the best line that fits the training data. In the case of linear regression, the “best” line is determined using a method called least squares. This method minimizes the sum of the squared residuals (the differences between the observed and predicted values).
