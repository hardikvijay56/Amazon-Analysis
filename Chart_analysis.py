import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"c:\users\hardi\downloads\Amazon Sale Report.csv")
df["date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(
    df["date"].dt.month
)["Amount"].sum()
monthly_sales.plot(kind="bar")

plt.title("Monthly_Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()