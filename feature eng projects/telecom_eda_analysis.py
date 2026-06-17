# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading Data 
df = pd.read_csv(r"C:\Users\syeda\OneDrive\Desktop\telecom.csv");


#Basic Data Info
print(df.columns) 


#Univariant Analysis 
#========================
Age= df["Age"].describe();
Tenure=df["Tenure in Months"].describe();
MonthlyGB=df["Avg Monthly GB Download"].describe()
totalRevenue=df["Total Revenue"].describe();

print(Age,Tenure,MonthlyGB, totalRevenue)


#Bivariant 
#====================
internettype_revenue = df.groupby(df["Internet Type"])["Total Revenue"].mean();
ContractCustomerStatus = df.groupby(["Contract","Customer Status"]).size().unstack();

print(internettype_revenue.max(),ContractCustomerStatus)


#Charts/plots  => Contract vs Customer 

ContractCustomerStatus.plot(kind="bar");
plt.title("Contract Vs Customer Status ");
plt.xlabel("Contract")
plt.ylabel("Count")
plt.show()

# plot of internettype_revenue
internettype_revenue.plot(kind="bar", color="black");
plt.title("Internet type Vs Total revenue")
plt.xlabel("Internet Type")
plt.ylabel("Total revenue")
plt.show()



#Observation 1. Fiber Optics generate more revenue 
 #           2.Month-Month User Churned More 

#MultiVariant Anlyses 
#=====================================
AvgMonthlyCharge= df.groupby(["Contract","Customer Status"])["Monthly Charge"].mean();

print(AvgMonthlyCharge)


# Correlation practice
# ====================================

MonthlyCharge_corr_revenu=df['Monthly Charge'].corr(df['Total Revenue'])
print(MonthlyCharge_corr_revenu)    #positive moderate correlation 

tenure_revenue=df['Tenure in Months'].corr(df['Total Revenue'])
print(tenure_revenue)    
#Observation :- sttrongly positive corr (customer stay longer generates high revenu)


#Charts 
#==========================
contract_counts = df["Contract"].value_counts()
contract_counts.plot(kind='bar')
plt.title("Contract Distribution")
plt.xlabel("Contract Type")
plt.ylabel("Count")

plt.show()


#Histogram 
#===================
age_plot=df["Age"]
age_plot.plot(kind="hist")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

#HeatMap (sns is not importing ?)
#==================
corr = df.corr(numeric_only=True)

sns.heatmap(corr)

plt.show()


#Null Vals / Outlier treatments 
#================================

df["Internet Type"] = df["Internet Type"].fillna("No Internet")
df["Internet Type"].isnull().sum()
