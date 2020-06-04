
import csv

csv_file_path = "sales2.csv" # a relative filepath
total_sales = 0 

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    for row in reader:
        print(row["product"], row["sales price"])
        total_sales = total_sales + float(row["sales price"])

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")
print("TOTAL SALES " + to_usd(total_sales))