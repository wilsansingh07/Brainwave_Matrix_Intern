# -*- coding: utf-8 -*-
"""brainware task 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VwZIUXBug7eXCCwME4GU2HzxozWI34nu
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd

df = pd.read_csv("shopsmart_sales_dataset.csv")

product_sales = df.groupby("Product").agg({
    "Quantity": "sum",
    "Total Price": "sum"
})

top_by_revenue = product_sales.sort_values(by="Total Price", ascending=False).head(5)
top_by_quantity = product_sales.sort_values(by="Quantity", ascending=False).head(5)

print("Top 5 Products by Revenue:")
print(top_by_revenue)

print("\nTop 5 Products by Quantity Sold:")
print(top_by_quantity)