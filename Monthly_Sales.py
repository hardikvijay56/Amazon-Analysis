import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\hardi\Downloads\Amazon Sale Report.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Amount"].sum()

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()