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

#2. Univariate Analysis
## univariate -> Analyzing one variable at a time (Oen column)

#2.1 Sales Distribution

def get_sales_distribution_chart(df):
    fig = px.histogram(df, x='Sales', nbins=50, title='Sales Distribution') #nbins -> number of bars
    return fig

# Conclusion:
#Sales are not uniform
#many small orders
#Few large orders

#2.2 Profit Distribution
def get_profit_distribution(df):
    fig = px.histogram(df, x='Profit', nbins=50, title='Profit Distribution')
    return fig

## profit can be negative
## Negative orders indicate loss
## Outliers may need removal
#2.3 Discount Distribution

def get_discount_distribution(df):
    fig = px.histogram(df, x='Discount', nbins=50, title='Discount Distribution')
    return fig
    ## Not many discoumts were give, we're good

#3. Bivariate Analysis
# Understand relationships between two columns

#3.1 - Sales vs Profit
def get_sales_vs_profit(df):
    fig = px.scatter(df, x='Sales', y='Profit', color='Category', title='Sales vs Profit')
    return fig
## High Sales != High Profit
## Some high sales orders still make a loss
## furniture losses looks more
## More consistency with tech products

#3.2 Sales by State
def get_sales_vs_state(df):
    state_sales = df.groupby('State')['Sales'].sum().reset_index()
    fig = px.bar(state_sales, x='State', y='Sales',title='Sales by State')
    return fig
##california sales are dominating
## remove the stores from west virginia - no sales at all

# 4. Time Series patterns
## trends across months/ years
# monthly = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
# fig = px.line(monthly, x = 'Month', y='Sales', color='Year', title='Monthly Sales Trend by Year')
# fig.show()
## November is good month in all years 
## Summers are dull across all years, monsoon / new year transition is extreemely good

#5. Segment Wise Analysis
# segment_sales = df.groupby('Segment')['Sales'].sum().reset_index()
# fig = px.bar(segment_sales, x='Segment', y='Sales', title='Sales by Segment')
# fig.show()

##Conclusion: 
# Consumer segment genrally dominates
# Corporate may have higher average order value

#6. Top/bottom Analysis 
# - Top -> set ascending = False; for the bottom -> set ascending = True
# top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
# fig = px.bar(top_states, x=top_states.index, y=top_states.values, title='Top 10 states by Sales')
# fig.show()

#Most loss making sub categories
# loss_items = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=True).head(10)
# fig = px.bar(loss_items, x=loss_items.index, y=loss_items.values, title='Top Loss making Sub categories')
# fig.show()
# We can discontinue certain categories
# items that require pricing fixes
# Need for better supplier negoatiation