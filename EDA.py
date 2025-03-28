#Import statements
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st
sns.set()

#Read in the dataframe
stocks = pd.read_csv('adjprice.csv')

#Set index to datetime, drop original date column
stocks.set_index(pd.to_datetime(stocks["Date"], format='%Y%m%d'), inplace=True)
stocks.drop(columns=["Date"], inplace=True)

#Calculate how many stocks there are 
num_stocks_list = []
for i in range(0,9459):
    num_stocks = len(stocks.iloc[i,:].dropna(axis=0))
    num_stocks_list.append(num_stocks)
print(min(num_stocks_list), max(num_stocks_list))

#Describe 
stocks.describe()

#Initial plotting
stocks_subset = stocks.loc[pd.Timestamp("1993-09-07"):pd.Timestamp("1994-09-07")].iloc[:,:2]
stocks_subset.plot.line(title = "1 year time period");

stocks_subset = stocks.loc[pd.Timestamp("1993-09-07"):pd.Timestamp("2019-07-31")].iloc[:,:2]
stocks_subset.plot.line(title = "Entire 26 year time period");

stocks_subset = stocks.loc[pd.Timestamp("2010-01-01"):pd.Timestamp("2013-01-01")].iloc[:,:2]
stocks_subset.plot.line(title = "2010 to 2013: the disapearance of both stocks");

stocks_total = stocks.sum(axis=1) #Not actually correct
mean = stocks_total.rolling('30d', center=True).mean()
mean.plot.line();
