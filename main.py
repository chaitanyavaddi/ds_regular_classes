import pandas as pd


df = pd.read_csv("/Users/chaitanyavaddi/Documents/01_met/datascience/ds_regular_classes/datasets/Sample_ Superstore.csv")

#1. Get 5 by 5 rows and columns within dataset
# print(df.head())

#2. Get datatypes of columns
# print(df.info())

#3. Summary Statistics - #mean, standard deviation, min/max values, unexpected values
# print(df.describe())

#4. Missing values - Empty entries
# print(df.isnull().sum())

#5. Duplicates - Exact same row appearing more than once
# Business impact - duplicate rows = wrong revenue calculation
# print(df.duplicated().sum())

# 6. Ouliers 
# very large or very small values

#Assigment
# Choose a dataset from kaggle
# Do priliminary analysis
# Fund data quality issues
