import pandas as pd
df = pd.read_csv(r"c:\users\hardi\downloads\Amazon Sale Report.csv")
print("\nTop 10 States by Quantity Sold:")
print("\nTop 10 States by Revenue:")
print(
    df.groupby("ship-state")["Amount"].sum()
    .sort_values(ascending=False)
    .head(10)
)
