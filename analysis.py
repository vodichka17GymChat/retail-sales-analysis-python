import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_project_001.csv")

df["revenue"] = df["unit_price"] * df["quantity"]

print(df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(5))

product_summary = df.groupby("product").agg({"quantity": "sum", "revenue": "sum"}).sort_values(by="revenue", ascending=False).head(5)

top_5 = product_summary.head(5)
plt.bar(top_5.index, top_5["revenue"])
plt.title("Top 5 Products by Revenue")

plt.xlabel("Product")
plt.ylabel("Revenue (€)")

plt.savefig("top_5_products.png", dpi=300, bbox_inches="tight")
plt.show()

