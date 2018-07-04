# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
data = pd.read_csv("/Users/FreddyCarlberg/crypto_collab/CryptoGeeks/data/Bitfinex_BTCEUR_trades_2018_02_02.csv")
data.head(10)
sns.set(style="darkgrid", context="talk", palette="Dark2")
short_rolling = data.rolling(window=20).mean()
from datetime import datetime 
import os
data[New_Date] = data["date"]/1000
print(f" Maximum date: {data["date"].max()}")
data.head(10)
newdates = data("date")/1000
newdates = df["date"]/1000
newdates = df.data("date")/1000
data["NEW_DATE"] = data["date"]/1000
data["DT"] = data["NEW_DATE"].map(lambda val:datetime.datime. 
fromtimestamp(val).
strftime("%Y-%m-%d"))
data["DT"] = data["NEW_DATE"].map(lambda val:datetime.datetime. 
fromtimestamp(val).
strftime("%Y-%m-%d"))
data["DT"] = data["NEW_DATE"].map(lambda val: datetime.datetime. 
fromtimestamp(val).
strftime("%Y-%m-%d"))
return datetime.fromtimestamp(date / 1000)
NewDate = datetime.fromtimestamp(date/1000) 
data["DT"] = data["NEW_DATE"].map(lambda val: datetime.datetime.fromtimestamp(val).strftime("%Y-%m-%d"))
def convert_dates(date):
    return datetime.fromtimestamp(date / 1000) 
data["date"] = data["date"].apply(convert_dates)
data.set_index("date", inplace=True) 
trades.sort_index(ascending=True, inplace=True) 
data.sort_index(ascending=True, inplace=True)
assert data["exchange"].nunique() ==1, "Multiple exchanges present"
assert data["symbol"].nunique() == 1, "Multiple symbols present"
data-head(10)
data.head(10)
data_features = data[["price", "amount", "sell"]]
exchange = data["exchanges"].iloc[0]
exchange = data["exchange"].iloc[0]
symbol = data["symbol"].iloc[0]
return exchange, symbol, data_features
return exchange, symbol, trade_features
return exchange
data-head(10)
data.head(10)
del data.NEW_DATE
del df.NEW_DATE
del data["NEW_DATE"]
data.head(10)
short_rolling = data.rolling(window=20).mean()
from movingaverage import movingaverage 
data["price"].mean()
long-term SMA = data["price"].mean()
long_term_SMA = data["price"].mean()
SRD1 = data.loc[[0,100], price]
price = data.iloc[price]
data
data.iloc[:,4]
data.iloc[:,5]
data.iloc[:,3]
prices = data.iloc[:,3]
result = (data.set_index("date") 
.groupby("market")["value"]
.rolling(10).mean()
.unstack("market"))
rollingmean = pd.rolling_mean(prices, 100)
rollingmean = prices.rolling(100).mean()
rollingmean
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'osx')
rollingmean = simplemovingaverage
fig = plt.figure()
x = data["date"]
data.plot(x="date", y="prices")
data.iloc[:,0]
data["date"]
date = [2018.02.02, 2018.02.03]
rollingmean
data.["date"]
data["date"]
data.reset_index()
rollingmean
date = data.iloc[:,0]
date
data
data1 = data.reset_index()
data1
date = data1.iloc[:,0]
date
prices
prices1 = data1.iloc[:,4]
prices1
plt.plot(date, prices1, color="g")
plt.xlabel("Time")
rollingmean
plt.close()
movingaverage = prices1.rolling(100).mean()
movingaverage
plt.plot(date, movingaverage, color="orange")
plt.xlabel("Time")
plt.ylabel("StandardMovingAverage")
plt.title("StandardMovingAverage")
plt.show()
get_ipython().run_line_magic('save', 'CryptoProject')
get_ipython().run_line_magic('save', 'CryptoProject.py')
get_ipython().run_line_magic('pinfo', 'save')
get_ipython().run_line_magic('save', '-r CryptoProject')
get_ipython().run_line_magic('save', '-r "CryptoProject"')
get_ipython().run_line_magic('s', '')
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', 'freddycryptoproject')
get_ipython().run_line_magic('save', 'CryptoGeeks')
get_ipython().run_line_magic('pinfo', '%save')
get_ipython().run_line_magic('save', 'freddys-file 1-108')
