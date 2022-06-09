# Credit-Card-Default-Detection



## https://cred-default-detector.herokuapp.com

(Used Flask , docker image and deployed on Heroku platform)

A demo of the project is given below:-

https://user-images.githubusercontent.com/96677288/172887599-abc2fedc-40f7-47f7-8c1f-a91ea3f91e5b.gif





### Introduction
Whenever we accept a credit card, we agree to certain terms and conditions including making our repayments by the due date listed on our credit card statement. When we miss the minimum payment by 6 months or more in a row, our credit card will be in default. In such situations, our credit card issuer will first send several notices via email or SMS and call us asking to make the repayment. If we do not make the payment after a stipulated period, they will close our account and report the default to the credit bureaus. This period may vary from one credit card provider to another. This tends to impact our credit score and it will be difficult for us to get approved for loans in the future. Once we are listed as a credit card defaulter, we become a risk for any credit obligation. 

### Goal
   The goal is to build a machine learning model that can predict whether a customer would commit a cred


it card default or not. It also aims to integrate the model and build a docker image for deployment on the Heroku Platform.
   
### Data Preprocessing
Visualized the data, multiple missing values and outliers detected. Missing values are being handled using various statistical parameters and also used randoom imputation. Interquartile Range were used to treat the outliers. Also the dataset was very imbalanced (mimority class has only around 10% of the total data points) so, minority class was Oversampled and majority class was UnderSampled and brought the minority class to 25% of the datapoints.

### Training 
 Used various ML Algorithms like Logistic Regression, SVM, RandomForest, Gradient Boosting etc. Since, the dataset was imbalanced, i have decided to get F1 macro score for the model evaluation. Also performed Randomized Search for hyperparameter tuning. I was abled to achieved F1 macro score of around 93$ on the test set.
 
 ![image](https://user-images.githubusercontent.com/96677288/172863243-38ac5fef-ce37-4ccf-9d26-f61b6b58d80d.png)

  Since, the dataset is still imbalanced after oversampling, i have used the macro type of f1 score. Macro is useful when the dataset is imbalanced because it calculates the f1 score per class (taking one class at a time)
