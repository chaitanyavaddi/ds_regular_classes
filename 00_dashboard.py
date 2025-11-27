import streamlit as st
from EDA import *
import pandas as pd

df = pd.read_csv("/Users/chaitanyavaddi/Documents/01_met/datascience/ds_regular_classes/Cleaned_Superstore.csv")

st.title('EDA Analyis by Chaitanya V')
st.plotly_chart(get_sales_distribution_chart(df))
st.write('''
    Conclusion:
    - Sales are not uniform
    - many small orders
    - Few large orders
''')
st.divider()
st.plotly_chart(get_discount_distribution(df))
st.plotly_chart(get_profit_distribution(df))
st.plotly_chart(get_sales_vs_profit(df))
st.plotly_chart(get_sales_vs_state(df))

