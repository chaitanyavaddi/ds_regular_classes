## Data Sources
# Category 1 - File Based Data Sources
# - Most real-world data arrives to a data team in files
# - Clients, business teams, CRMs, downloaded datasets, software exports
# - Each file will ahve tis own structure and pandas can read all of them

##1. CSV Files (Comma Separated Values)
# - CSV is a plain text file
# - Columns are seperated by commas, soemtimes ; or |
# - Simple, universal, lightweight

#syntax:
# import pandas as pd
# df = pd.read_csv('diabetes.csv', sep=';', encoding='latin1')
# #sep -> custom seperators
# #encoding -> Fix bad encoding problems
# #header = None -> No header will be in df
# print(df)

## 2. Excel files (.xls, .xlsx)
# Excel is still the language of business
# - Excel supports multiple sheets
# import pandas as pd
# df = pd.read_excel('file.xlsx', sheet_name='Sales')
# - Specify columns
# pd.read_excel('file.xlsx', usecols="A:D")
# - Write to excel
# df.to_excel('output.xlsx', index=False)

## 3. JSON Files
# JSON - Javscript Object Notation
# import pandas as pd
# data = pd.read_json("sample.json")
# df = pd.json_normalize(data)
# print(data.head())

## 4. XML (Older enterprises, banks, telecom)
# Structure
# Tab based
# Eg. <record><name>John</name><age>67</age></record>
# import pandas as pd
# df = pd.read_xml("sample.xml")
# print(df.head())

## 5. Parquet (Big data format)
# Used in data lakes, Spark, Snowflake, BigQuery, databricks
# - Columnar format - very fast, compressed, Optimized for big data
# Pandas can read parquet file
# import pandas as pd
# df = pd.read_parquet('userdata.parquet')
# df.to_parquet('output.parquet') #to export
# print(df.info())

## 6. TXT Files
# - Server logs, chat logs, sensor logs
# with open('sample.txt') as f:
#     lines = f.readlines() #List of lines
# import pandas as pd
# df = pd.DataFrame(lines, columns=['log'])
# print(df.head())

## 7 - HTML TABLE Extraction
# Pandas finds tables automatically
# import pandas as pd
# df = pd.read_html('sample.html')
# print(df)


#Assing:
# Read this https://gist.githubusercontent.com/iwek/4177628/raw/03d302f6461490bea7dcee09b96076053148a1be/sample.log
# Load into csv and save

#Extract world population table and show top 5 countries 
# worldometers.info/world-population