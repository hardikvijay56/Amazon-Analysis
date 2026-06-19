import pandas as pd
df = pd.read_csv(r"c:\users\hardi\Downloads\Amazon Sale Report.csv")
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(
    df["Date"].dt.month
)["Amount"].sum()
print(monthly_sales)
