import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("btc_price_history.csv")
df["date"] = pd.to_datetime(df["date"])
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["btc_usd_price"], marker="o")
plt.title("Bitcoin Price History")
plt.xlabel("Date")
plt.ylabel("BTC Price (USD)")
plt.grid(True)
plt.tight_layout()
plt.savefig("btc_price_history.png")
