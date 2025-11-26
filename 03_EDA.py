#1. Dataset Overview -> Refer Dataset_loading.py
#2. Univariate Analysis
#3. Bivariate Analysis
#4. Time Series patterns
#5. Segment wise / region wise Analysis
#6. Top/Bottom Analysis
#7. Protitability Analysis
#8. Discount Impact Analysis
#9. Correlation Analysis
#10. Final Business Recommendations
import pandas as pd
import plotly.express as px

df = pd.read_csv("/Users/chaitanyavaddi/Documents/01_met/datascience/ds_regular_classes/Cleaned_Superstore.csv")

#2. Univariate Analysis
## univariate -> Analyzing one variable at a time (Oen column)

#2.1 Sales Distribution
# fig = px.histogram(df, x='Sales', nbins=50, title='Sales Distribution') #nbins -> number of bars
# fig.show()
    # Conclusion:
    #Sales are not uniform
    #many small orders
    #Few large orders

#2.2 Profit Distribution
# fig = px.histogram(df, x='Profit', nbins=50, title='Profit Distribution')
# fig.show()
    ## profit can be negative
    ## Negative orders indicate loss
    ## Outliers may need removal
#2.3 Discount Distribution
# fig = px.histogram(df, x='Discount', nbins=50, title='Discount Distribution')
# fig.show()
    ## Not many discoumts were give, we're good

#3. Bivariate Analysis
# Understand relationships between two columns

#3.1 - Sales vs Profit
# fig = px.scatter(df, x='Sales', y='Profit', color='Category', title='Sales vs Profit')
# fig.show()
## High Sales != High Profit
## Some high sales orders still make a loss
## furniture losses looks more
## More consistency with tech products

#3.2 Sales by State
# state_sales = df.groupby('State')['Sales'].sum().reset_index()
# fig = px.bar(state_sales, x='State', y='Sales',title='Sales by State')
# fig.show()
##california sales are dominating
## remove the stores from west virginia - no sales at all

# 4. Time Series patterns
## trends across months/ years
# monthly = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
# fig = px.line(monthly, x = 'Month', y='Sales', color='Year', title='Monthly Sales Trend by Year')
# fig.show()
## November is good month in all years 
## Summers are dull across all years, monsoon / new year transition is extreemely good