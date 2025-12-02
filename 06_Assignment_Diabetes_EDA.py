
# column          Meaning
# Pregnancies ->  Number of Pregnancies
# Glucose     ->  Plasma glucose concentratio
# BloodPressure -> Diastolic BP
# SkinThickness -> Skin fold thickness
# Insulin -> 2-Hour serum insulin
# BMI -> Body mass index
# DiabetesPedigreeFunction -> Diabetes pedigree function
# Age -> Age in years
# Outcome -> 0 - non diabetic, 1 -> diabetic

import pandas as pd
import numpy as np

df = pd.read_csv("diabetes.csv")

#Step 1
# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())

#Insights:
## - 768 rows, 9 columns
## No missing NULLs in csv
## But some columns contain 0 values that are impossible
## Eg. BP=0, BMI=0 -> we will treat them as missing

df = df.drop_duplicates()

#Step 2: check missing values

cols = ['Glucose', 'BloodPressure', "SkinThickness", "Insulin", "BMI"]

print((df[cols] == 0).sum())

#Following are missing values:
# Glucose            5
# BloodPressure     35
# SkinThickness    227
# Insulin          374
# BMI               11

df[cols] = df[cols].replace(0, np.nan)

# print(df.isna().sum())
# df.to_csv("Cleaned_Diabetes.csv", index=False)

#EDA
#1. Univariate Analysis

#Outcome Distribution
import plotly.express as px

fig = px.histogram(df, x='Outcome', color='Outcome', title='Outome Distribution')

fig.show()


