## 2. Database Sources - Category 2
# - Why database exist?
# SQL vs NoSQL
# Connect to DB via Python
# Read data into Pandas
# Write data back to DB


## 1. SQL Databases (Structured)
## Store large datasets
## ACID transactions (Atomicity, Consistency, Isolation, Durability)
## Reliable, Secure, Index & Query optimised

# -1.1 PostgresSQL
# import pandas as pd
# import psycopg2
# db_url = 'postgresql://postgres.ncciqlxhemfpizfqxqot:123456789@aws-1-ap-south-1.pooler.supabase.com:5432/postgres'
# conn = psycopg2.connect(db_url)
# df = pd.read_sql("SELECT * FROM products", conn)
# df.to_sql("products", conn, if_exists="append", index=False)

# -1.2 MYSQL
# import mysql.connector
# import pandas as pd
# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='12345678',
#     database='salesdata'
# )
# df = pd.read_sql("SELECT * FROM Daily_Sales", conn)
# df = df.fillna(0)
# df.to_sql('Daily_Sales', con=conn, if_exists='replace', index=False, schema='salesdata')
# print(df)
# - SQLite

# - MSSQL
# - Oracle


