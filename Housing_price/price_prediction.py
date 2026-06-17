# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:12:09 2026

@author: syeda
"""

import pandas as pd;
from sklearn.model_selection import train_test_split
import numpy as np;
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from datetime import datetime
import matplotlib.pyplot as plt;

df=pd.read_csv(r"OneDrive\Desktop\Datasci\Housing_price\real_estate_dataset.csv")
print(df.head(5))
print(df.shape)
print(df.isna().sum())

current_year = datetime.now().year
df["House_Age"] = current_year - df["Year_Built"]



X=df.drop(columns=["ID","Price"])
Y=df["Price"]

x_test , x_train , y_test, y_train = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
    )

model=LinearRegression()
model.fit(x_train,y_train)

predicted_price=model.predict(x_test)


results = pd.DataFrame({
    "Actual_Price": y_test,
    "Predicted_Price": predicted_price
})

print(results.head(5))


mae=mean_absolute_error(y_test, predicted_price)
mse=mean_squared_error(y_test, predicted_price)
print("mse:" ,mse)
print("mae:" ,mae)




all_pridictions = model.predict(X)
df["all_Predicted_price"]=all_pridictions


#//plots 

plt.plot(X,Y)m
