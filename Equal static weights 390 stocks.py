#Construct a list of strings representing the beginning of each year in datetime notation
years = ["2010-07-31", "2011-07-31", "2012-07-31", "2013-07-31", "2014-07-31", "2015-07-31", "2016-07-31", "2017-07-31","2018-07-31", "2019-07-31"]

#Keep track of daily portoflio returns
all_portfolio_returns = pd.Series(dtype=float)

#Set risk-free rate
risk_free_rate = 0.02 

investment_value = 10000
list_of_investment_values = [10000]

weights = [1/stocks.shape[1]]*stocks.shape[1]

#At the end of every year, the performance of each stock is evaluated.
for i in range(len(years)-1):

    #Retrieve stocks for next year
    stocks_next_year = stocks.loc[pd.Timestamp(years[i]):pd.Timestamp(years[i+1])]  
    #Calculate return
    daily_returns_next_year = stocks_next_year.pct_change().dropna()
    portfolio_returns = daily_returns_next_year @ weights
    final_profit = (portfolio_returns + 1).prod() - 1
    #Add to daily portfolio return list
    all_portfolio_returns = pd.concat([all_portfolio_returns, portfolio_returns])
    #Update investment value
    investment_value = investment_value*(1+final_profit)
    list_of_investment_values.append(investment_value)
    #Print profit for the next year
    print(f"Final profit for portfolio during {years[i][0:4]} - {years[i+1][0:4]} :", final_profit, "%")
    #Print value of investment 
    print(f"Value of investment after July {years[i+1][0:4]}:", investment_value)

# Convert risk-free rate to daily
risk_free_daily = risk_free_rate / 365

# Calculate daily Sharpe ratio
sharpe_daily = (all_portfolio_returns - risk_free_daily).mean() / all_portfolio_returns.std()

# Annualize Sharpe
sharpe_annualized = sharpe_daily * np.sqrt(365)

print(f"Annualized Sharpe Ratio (2010-2019): {sharpe_annualized:.2f}")

