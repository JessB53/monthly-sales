

import os
import pandas
 
csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "sales.csv") 
df = pandas.read_csv(csv_filepath)
# print(type(df)) #> <class 'pandas.core.frame.DataFrame'>
# print(df.head()) #> prints first few rows

sales = df.to_dict("records") #create list from dataframe

#Sum sales for entire data set 
total_sales = 0
for x in sales:
    total_sales = total_sales + x["sales price"]

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

total_sales = to_usd(total_sales)
#print(total_sales)

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")

print("TOTAL SALES: " ,total_sales)