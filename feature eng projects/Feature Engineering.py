# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:59:26 2026

@author: syeda
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading Data 
df = pd.read_csv(r"C:\Users\syeda\OneDrive\Desktop\telecom.csv");


#Basic Data Info
print(df.columns) 

#Feature Engineering 

#1- Bining 
print(df['Age Bucket'].isna().sum()) #No Missing vals 

def Age_group(age):
    if age <25:
        return "Young"
    elif age<50:
        return "Adult"
    else:
        return "Old"

df["Age Group"] = df["Age"].apply(Age_group)

print(df["Age Group"].value_counts() )

#Revenue Per Month =Total Revenue % Tenure in Months

df["Revenue per Month"] = df["Total Revenue"]%df["Monthly Charge"]

print(df["Revenue per Month"].isna().sum())




#Label Hot encoding 

#!Gender  male-0 , female-1
df["Gender"] = df["Gender"].map({
    "Male": 0,
    "Female": 1
})
#One hot Encoding 
InternetTypes= pd.get_dummies(df,columns=['Internet Type'], dtype=int)
InternetTypes.filter(like='Internet Type').head()

ContractType=pd.get_dummies(df,columns=['Contract'],dtype=int)
ContractType.filter(like="Contract").head()


#Freq/Count encoding
counts=df["City"].value_counts()
df['City Counts']=df["City"].map(counts)
print(df[['City','City Counts']].head(10))


#Premium user 
avg_charge = df["Monthly Charge"].mean()
print(avg_charge)
    
df.loc[(
        (df['Internet Type']=='Fiber Optic') & (df['Monthly Charge'] >= 63)
        ),"Premium User"]="Yes"

df['Premium User'] = df['Premium User'].fillna("No")
df["Premium User"].value_counts()

#High Paying cutsomers are churning more or not
premium_status = pd.crosstab(
    df["Premium User"],
    df["Customer Status"]
)

print(premium_status)
premium_status.plot(kind="bar")

plt.title("Premium User vs Customer Status")
plt.xlabel("Premium User")
plt.ylabel("Number of Customers")

plt.show()

premium_status.div(premium_status.sum(axis=1), axis=0) * 100

#Observation :_ Premium users have ~40.8% churn rate vs ~16% for non-premium users.


#Ratio , projection score 
security = df["Online Security"].map({"Yes":1, "No":0})
backup = df["Online Backup"].map({"Yes":1, "No":0})
support = df["Premium Tech Support"].map({"Yes":1, "No":0})

df['Protection Score'] = security+  backup+ support;

print(df['Protection Score'].value_counts())

#Bivariant analyses 
protection_churn = pd.crosstab(
    df["Protection Score"],
    df["Customer Status"],
    normalize="index"
) * 100

protection_churn.plot(kind="bar")

plt.title("Protection Score vs Customer Status")
plt.xlabel("Protection Score")
plt.ylabel("Percentage")

plt.show()

#Observation :_ those customers whos protection schore are less have churend more


#Tenure 3 types , risky , loyal , regular

print(df["Tenure Bucket"].value_counts())


def tenure_group(months):
    if months <= 12:
        return "New"
    elif months <= 36:
        return "Regular"
    else:
        return "Loyal"

df["Tenure Group"] = df["Tenure in Months"].apply(tenure_group)

df['Tenure Group'].value_counts()


# Bivariant Analysis - Tenure Group vs Customer Status

tenure_churn = pd.crosstab(
    df["Tenure Group"],
    df["Customer Status"],
    normalize="index"
) * 100

print(tenure_churn)

tenure_churn.plot(kind="bar")

plt.title("Tenure Group vs Customer Status")
plt.xlabel("Tenure Group")
plt.ylabel("Percentage")

plt.show()

# Observation:
# Loyal customers churn less than New customers.


#Revenue Tier 

df["Revenue Tier"] = pd.cut(
    df["Revenue per Month"],
    bins=3,
    labels=["Low", "Medium", "High"]
)

print(df["Revenue Tier"].value_counts())


revenue_churn = pd.crosstab(
    df["Revenue Tier"],
    df["Customer Status"],
    normalize="index"
) * 100

print(revenue_churn)

revenue_churn.plot(kind="bar")

plt.title("Revenue Tier vs Customer Status")
plt.xlabel("Revenue Tier")
plt.ylabel("Percentage")

plt.show()

# Observation: Medium and High Revenue customers have higher churn percentages.


# Ordinal Encoding
mapping = {
    "New": 1,
    "Regular": 2,
    "Loyal": 3
}

df["Tenure Group Encoded"] = df["Tenure Group"].map(mapping)

print(df[["Tenure Group", "Tenure Group Encoded"]].head())



# Log Transformation

df["Log Revenue"] = np.log1p(df["Total Revenue"])

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.hist(df["Total Revenue"])
plt.title("Before Log Transform")

plt.subplot(1,2,2)
plt.hist(df["Log Revenue"])
plt.title("After Log Transform")

plt.tight_layout()
plt.show()


# Square Root Transformation


df["Sqrt Revenue"] = np.sqrt(df["Total Revenue"])

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.hist(df["Total Revenue"])
plt.title("Before Sqrt Transform")

plt.subplot(1,2,2)
plt.hist(df["Sqrt Revenue"])
plt.title("After Sqrt Transform")

plt.tight_layout()
plt.show()



