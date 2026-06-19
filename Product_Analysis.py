import pandas as pd
df = pd.read_csv(r"c:\users\hardi\downloads\Amazon Sale Report.csv")
print("\ntop categories by Quantity Sold:")
print(
    df.groupby("Category")["Qty"].sum()
    .sort_values(ascending=False)
)
print("\ntop categories by Revenue:")
print(
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)
print("\nMost popular Sizes:")
print(
    df["Size"]
    .value_counts()
)