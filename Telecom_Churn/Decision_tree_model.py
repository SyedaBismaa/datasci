# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:35:23 2026

@author: syeda
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
    )

df = pd.read_csv(r"C:\Users\syeda\OneDrive\Desktop\Datasci\Telecom_Churn\Telecom_woe_converted.csv")


print(df.head(6))


X=df.drop(columns=["Customer ID","Dummy_Customer_id","Target"])
y=df["Target"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
    )
print(df["Age_Bucket_Converted"].unique())

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
    )

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

plt.figure(figsize=(20,10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["No Churn", "Churn"],
    filled=True
)

plt.show()