import pandas as pd

df = pd.read_csv("/Users/chaitanyavaddi/Documents/01_met/datascience/ds_regular_classes/datasets/Sample_ Superstore.csv")

###########################################
#Step 1 - Remove duplicates Rows
# Duplicate rows inflate sales and profit
df = df.drop_duplicates()
###########################################

###########################################
#Step 2 - Convert Dates to DateTime
# Python treats dates as text by default
# Must convert to datetime to extract year, month, day
## dd-mm-yyy or dd/mm/yyyy or mm/dd/yyyy or mm-dd-yyyy
# format = 'mixed' -> tells pandas to handle them automatically
# dayfirst = True -> ensures formatting automaticlaly with day first
## Ef. 12/03/2017 -> 12 March, Not Dec 03
# errors = 'coerce' - invalid dates become NaT instead of breakign our code
# # print(df)
## 1. Normlization
df['Order Date'] = df['Order Date'].astype(str).str.replace('-','/')
## 2. Conversion
df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)
df['Ship Date'] = df['Ship Date'].astype(str).str.replace('-','/')
df['Ship Date'] = pd.to_datetime(
    df['Ship Date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)
# Note: feature engineering -> creating new columns that add meaning to analysis
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days
###########################################


###########################################
#Step 3 - Handling Missing values 
df = df.fillna(0)
###########################################

###########################################
#Step 4 - Clean categorial Columns
## Sometimes data has extra spaces, case inconsistency, spelling variations
df['Ship Mode'] = df['Ship Mode'].str.strip().str.title()
df['State'] = df['State'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()
###########################################

###########################################
#Step 5 - Outlier Detection 
## A value that is extremely higher or lower than normal
## Outliers distort averages, charts and correlations
## IQR Method - a standard statistical rule
Q1 = df['Profit'].quantile(0.25)
Q3 = df['Profit'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df['Profit'] >= lower) & (df['Profit'] <= upper)]
print(df.describe())
###########################################


###########################################
#Step 6 - Create Business Columns
#6.1 Profit Margin % -  (profit / sales) * 100
df['Profit Margin %'] = (df['Profit'] / df['Sales']) * 100
print(df['Profit Margin %'])

#6.2  Extract yeat & Month (Seasonal Analysis)
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

#6.3 High Discount Flag (Useful for business reports)
df['High Discount'] = df['Discount'].apply(lambda x: 1 if x > 0.3 else 0)
###########################################

###########################################
#Step 7 -  Save Clean file
df.to_csv("Cleaned_SuperStore.csv", index=False)
print(df)
###########################################
