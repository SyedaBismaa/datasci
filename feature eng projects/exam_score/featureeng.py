# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:10:15 2026

@author: syeda Bisma
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:/Users/syeda/OneDrive/Desktop/Datasci/feature eng projects/Exam_Score_Prediction.csv")

#Basic data Info
print(df.head())
print(df.columns)

# Gender (One hot encoding)

gender_encoded=pd.get_dummies(df,columns=['gender'], dtype=int);
print(gender_encoded.filter(like="gender").head())


#StudyHourse Grouping
print(df["study_hours"].describe())

def study_group(hours):
    if hours <=2:
        return "Low"
    elif hours <=6:
        return "Average"
    else:
        return "High"
    
df["study_group"] = df["study_hours"].apply(study_group)

print(df["study_group"].value_counts())

#Attendance group

print(df['class_attendance'].describe())

def attendance_group(attendance):
    if attendance <=50:
        return "Low"
    elif attendance <=70:
        return "Medium"
    else:
        return "High"
    
df['attendance_group']=df['class_attendance'].apply(attendance_group)
df['attendance_group'].head()

#Sleep hrs and sleep quality
print(df['sleep_hours'].describe())
def sleep_group(hours):
    if hours <=6:
        return "Low sleep"
    elif hours<=8:
        return "Healthy sleep"
    else:
        return "long sleep"
df["Health"]=df['sleep_hours'].apply(sleep_group)


print(df['sleep_quality'].value_counts())


#Internet acess encoding
df['internet_access_encoding'] = df['internet_access'].map({'yes':1, 'no':0})


#Study Methos 
print(df["study_method"].value_counts())
study_method_encoded= pd.get_dummies(df,columns=['study_method'], dtype=int)
print(study_method_encoded.filter(like='method_').head())

#Facility rating (ordinal endoing)
df['facility_rating'].value_counts()
df['facility_encoded']=df['facility_rating'].map({'low':0,'medium':1,'high':2})

#exam score
df['exam_score'].describe()

def score_group(marks):
    if marks<=40:
        return "Low"
    elif marks<= 70:
        return "average"
    else:
        return "high"
df['score_group']=df['exam_score'].apply(score_group)
print(df["score_group"].value_counts())

#Study Efficiency=Exam Score / Study Hours
df['study_efficency'] = df['exam_score'] / df['study_hours']
df['study_efficency'].describe()   #outliers detected
df["study_efficency"].sort_values(ascending=False).head(10)


df[['study_hours','exam_score','study_efficency']]\
.sort_values('study_efficency', ascending=False)\
.head(10)



#Analysis 
gender_vs_course= pd.crosstab(
    df["gender"],
    df["course"]
)
gender_vs_course.plot(kind='bar')
plt.title('Gender & Course')
plt.xlabel('gender')
plt.ylabel('course')
plt.show()

#Observation : equal distribution , all courses have balenced gender ratio


study_vs_score=pd.crosstab(
    df['study_group'],
    df['score_group'],
    normalize='index'
    )*100

study_vs_score.plot(kind='bar')
plt.title('Study Hours vs Score')
plt.xlabel('study_group')
plt.ylabel("Percentage")
plt.show()

#Observation : Students who study more hours tend to achieve higher exam scores

attendance_vs_score=pd.crosstab(
    df['attendance_group'],
    df['score_group'],
    normalize='index'
    )*100

attendance_vs_score.plot(kind='bar')
plt.title('attendance vs Score')
plt.xlabel('Ateendance')
plt.ylabel('score')
plt.show()

#observation :-Students with higher class attendance tend to achieve better exam scores

sleep_vs_score=pd.crosstab(
    df['Health'],
    df['score_group'],
    normalize='index'
    )*100

sleep_vs_score.plot(kind='bar')
plt.title('Sleep Quality vs Score')
plt.xlabel("Sleep  Quality")
plt.ylabel("score ")
plt.show()

#Observation :- Students with healthy and longer sleep durations show a higher percentage
#of high scorers, while low-sleep students are more likely to achieve lower scores.


studyMethod_vs_score=pd.crosstab(
    df['study_method'],
    df['score_group'],
    normalize='index'
    )*100

studyMethod_vs_score.plot(kind='bar')
plt.title('study method vs Score')
plt.xlabel("Study Method")
plt.ylabel("score ")
plt.show()

#observation : group study is more  effective than other study methods in this dataset.


high_score_pct = pd.crosstab(
    [df["attendance_group"], df["Health"]],
    df["score_group"],
    normalize="index"
) * 100

high_score_pct["high"].sort_values().plot(
    kind="barh",
    figsize=(10,5)
)

plt.title("High Score Percentage by Attendance and Sleep")
plt.xlabel("Percentage of High Scorers")
plt.ylabel("Attendance + Sleep Group")

plt.show()

#Observation : Students with healthy or longer sleep durations generally show a higher 
#percentage of high scorers, while low-sleep students are more likely to have lower scores.

course_method = pd.crosstab(
    [df["course"], df["study_method"]],
    df["score_group"],
    normalize="index"
) * 100

course_method["high"].sort_values().plot(
    kind="barh",
    figsize=(10,6)
)

plt.title("High Score % by Course and Study Method")
plt.xlabel("Percentage of High Scorers")
plt.ylabel("Course + Study Method")
plt.show()

#Observation :- Group study and coaching methods are associated with a higher proportion
# of high scorers, whereas self-study shows a comparatively lower proportion of
# high scorers.


attendance_internet = pd.crosstab(
    [df["attendance_group"], df["internet_access"]],
    df["score_group"],
    normalize="index"
) * 100

attendance_internet["high"].sort_values().plot(
    kind="barh",
    figsize=(10,5)
)

plt.title("High Score % by Attendance and Internet Access")
plt.xlabel("Percentage of High Scorers")
plt.ylabel("Attendance + Internet")
plt.show()
#Observation:-students with high attendance consistently achieve better scores regardless of internet availability.

sleep_method = pd.crosstab(
    [df["Health"], df["study_method"]],
    df["score_group"],
    normalize="index"
) * 100

sleep_method["high"].sort_values().plot(
    kind="barh",
    figsize=(10,6)
)

plt.title("High Score % by Sleep and Study Method")
plt.xlabel("Percentage of High Scorers")
plt.ylabel("Sleep + Study Method")
plt.show()

#Observaion:- Students who combine healthy sleep habits with structured study methods
#such as coaching or group study tend to have the highest percentage of high scorers



#The analysis suggests that attendance, study hours, sleep habits, and 
#study methods are important factors associated with exam performance.
#Among these, attendance appears to have the strongest relationship with 
#higher exam scores, while group study and coaching emerge as the most effective 
#study approaches in this dataset.