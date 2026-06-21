# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:37:02 2026

@author: syeda
"""

import pandas as pd

df = pd.read_csv("indeed_jobs.csv")


print(df["Job_Title"].value_counts().head(10))
print(df["Location"].value_counts().head(10))
print(df["Location"].value_counts().head(10))
print(df["Company_Name"].value_counts().head(10))