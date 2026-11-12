import pandas as pd
import matplotlib.pyplot as plt

data = {
    "product": ["Phone", "Nick_Air_Max", "Rice", "Harry_Potter", "Samsung_TV", 
                "Coke", "Jersy", "Face_Moisturizer", "Dinning_Table", "Chicken",
                "Headphones", "Notebook", "Tshirt", "Rollon", "Soap", "Pot"],
    "category": ["Electronics", "Footwear", "Groceries", "Books", "Electronics",
                 "Beverage", "Sports", "Skincare", "Furniture", "Groceries",
                 "Electronics", "Stationary", "Wears", "Deodorants", "Household",
                 "Kitchen_Utensil"],
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
            "Sunday", "Monday", "Friday", "Tuesday", "Saturday", "Wednesday",
            "Sunday", "Tuesday", "Monday", "Friday"],
    "cost_price": [150000, 22000, 37000, 2000, 280000, 250, 6000, 15000, 40000,
                   5000, 6000, 500, 7000, 1500, 1400, 15000],
    "selling_price": [200000, 30000, 50000, 5000, 350000, 500, 5000, 20000, 50000,
                   15000, 20000, 1000, 15000, 3000, 2000, 30000],
    "quantity": [50, 70, 50, 100, 20, 100, 40, 50, 10, 30, 50, 150, 40, 60, 80, 15]
}

cl = pd.DataFrame(data)

# adding a column for profit
cl["profit"] = (cl["selling_price"] - cl["cost_price"]) * cl["quantity"]

# adding another column for sales_amount
cl["sales_amount"] = cl["selling_price"] * cl["quantity"]
pd.set_option("display.max_columns", None)
print(cl)

# BUSINESS QUESTIONS
# Product that generated highest profit
highest_profit_product = cl.groupby("product")["profit"].sum().idxmax()
print("\n Product with Highest Profit")
print(highest_profit_product)

# Insight:
# Phone generated the highest profit, indicating strong sales performance.

# Category that generated highest Sales_Amount
highest_category_sale = cl.groupby("category")["sales_amount"].sum().idxmax()
print("\n Category with Highest Sales_Amount")
print(highest_category_sale)

# Insight:
# The Electronics category recorded the highest sales amount, suggesting that
# high-value electronic products contributed significantly to the supermarket's revenue.

# Day with highest sales
highest_sale_by_day = cl.groupby("day")["sales_amount"].sum().idxmax()
print("\n Day with Highest Sales")
print(highest_sale_by_day)

# Insight:
# Monday generated the highest sales revenue, indicating strong customer activity at the 
# start of the week

# Total Sales Amount
print("\n Total Sales Amount")
print(cl["sales_amount"].sum())

# Insight
# The total sales amount represents the overall revenue generated

# Product with Highest Quantity Sold
product_highest_quantity = cl.groupby("product")["quantity"].sum().idxmax()
print("\n Product with Highset Quantity Sold")
print(product_highest_quantity)

# Insight:
# Product with highest quantity sold was identified based on total units sold

# Category that Performs Worst
worst_category = cl.groupby("category")["sales_amount"].sum().idxmin()
print("\n Category that Performed Worst")
print(worst_category)

# Insight:
# The worst performing category was determined based on total sales revenue

# VISUALIZATION

# LINE CHART
# plotting profit by product

plt.figure(figsize=(18,5))

plt.subplot(1,3,1)
cl.groupby("product")["profit"].sum().plot(kind="line", marker='o')
plt.title("Profit by each Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.xticks(rotation=45)

# BAR CHART
# plotting Sales by Day

# Arrange days correctly
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
             "Saturday", "Sunday"]
sales_day = cl.groupby("day")["sales_amount"].sum()
sales_day = sales_day.reindex(day_order)
plt.subplot(1,3,2)
sales_day.plot(kind="bar")
plt.xlabel("Day")
plt.ylabel("Sales Amount")
plt.title("Sales Made Per Day")
plt.xticks(rotation=45)

# PIE CHART
# plotting Category Distribution by Sales_amount
plt.subplot(1,3,3)
cl.groupby("category")["sales_amount"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Distribution")
plt.ylabel("")

plt.tight_layout()
plt.show()





