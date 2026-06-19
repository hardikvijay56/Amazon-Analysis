import pandas as pd
df = pd.read_csv(r"c:\users\hardi\downloads\Amazon Sale Report.csv")
print("\nFulfilment Method Count:")
print(
     df["Fulfilment"]
     .value_counts()
)
print("\nFulfilment Revenue:")
print(
    df.groupby("Fulfilment")[("Amount")].sum()
    .sort_values(ascending=False)
)