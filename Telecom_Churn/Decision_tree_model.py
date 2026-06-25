# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:35:23 2026

@author: syeda
"""

# Importing required libraries
import pandas as pd
import numpy as np

# Splitting dataset and performing cross validation
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

# Decision Tree model
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

# Model evaluation metrics
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# For plotting the decision tree
import matplotlib.pyplot as plt


# Load Dataset --------------------
df = pd.read_csv(
    r"C:\Users\syeda\OneDrive\Desktop\Datasci\Telecom_Churn\Telecom_woe_converted.csv"
)

print(df.head(6))
print(df.columns)


#  Feature Selection --------------------
# X contains all independent features
# y contains the target column
X = df.drop(columns=["Customer ID", "Dummy_Customer_id", "Target"])
y = df["Target"]


#  Train Test Split --------------------
# Splitting dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Checking values of Age Bucket feature
print(df["Age_Bucket_Converted"].unique())


# Model Creation
# Creating Decision Tree with tuned hyperparameters
model = DecisionTreeClassifier(
    max_depth=3,
    min_samples_split=20,
    min_samples_leaf=10,
    random_state=42
)

# Training the model
model.fit(X_train, y_train)


#  Prediction --------------------
# Predicting target values for test dataset
y_pred = model.predict(X_test)


#  Model Evaluation --------------------
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


# K-Fold Cross Validation --------------------
kfold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


#  Stratified K-Fold --------------------
# Maintains the same class distribution in every fold
kfold2 = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# Cross Validation --------------------
score = cross_val_score(
    model,
    X,
    y,
    cv=kfold2,
    scoring="accuracy"
)

print("Accuracy of each fold:", score)
print("Average Accuracy:", score.mean())


#Decision Tree Visualization --------------------
plt.figure(figsize=(20, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["No Churn", "Churn"],
    filled=True
)

plt.show()


# Predict Entire Dataset --------------------
# Predicting churn for all customers
all_predictions = model.predict(X)

# Adding predictions to the original dataframe
df["Predicted_Result"] = all_predictions


#  Save Final Dataset --------------------
df.to_csv(
    r"C:\Users\syeda\OneDrive\Desktop\Datasci\Telecom_Churn\Telecom_Predicted.csv",
    index=False
)

print("File Saved Successfully!")