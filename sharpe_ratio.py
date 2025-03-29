stock = pd.read_csv('Stock_portfolio_data.csv')

stock_1997 = stock.iloc[0:1577,:]
# Subset dataframe to only include years 1993-1997.

stock_cleaned = stock_1997.dropna(axis=1, how='any')
# Drop all NA or missing values.

date_time_format = stock_cleaned.set_index(pd.to_datetime(stock_cleaned["Date"], format='%Y%m%d'))
# set the dataframe's date column to be in date time format.

stocks_return_percent = date_time_format.pct_change().dropna()
# Convert the dataframe to have the daily percentage change for each stock.

stocks_return_percent = stocks_return_percent.drop('Date', axis=1)
# Drop the date.

mean_stock_return_pct = stocks_return_percent.mean()
# Find the average daily percentage change for each stock.

top_5_returns = mean_stock_return_pct.nlargest(5)
# determine the top 5 stocks that have the highest average percentage return for each day.

print(top_5_returns)

top_5_returns_bad = mean_stock_return_pct.nsmallest(5)
# do the same but with top 5 worst stocks

print(top_5_returns_bad)

std_pct_dailychange =  stocks_return_percent.std()
# Now try and find the standard deviation/risk/volatility for each stock.

sharpe_ratio = mean_stock_return_pct/std_pct_dailychange
# Find the sharpe ratio for each stock.

top_5_std = std_pct_dailychange.nlargest(5)
# Find top 5 most volatile stocks.

top_5_sharpe_ratio = sharpe_ratio.nlargest(5)
# Find top 5 best sharpe ratio stocks.

print(top_5_std)
print(top_5_sharpe_ratio)
