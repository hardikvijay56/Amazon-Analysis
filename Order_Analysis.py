import pandas as pd
df = pd.read_csv(r"c:\users\hardi\downloads\Amazon Sale Report.csv")
print("\nOrder Status distibution:")
print(
    df["Status"]
    .value_counts()
)
