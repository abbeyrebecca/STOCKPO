#Construct a list of strings representing the beginning of each year in datetime notation
years = ["2009-07-31", "2010-07-31", "2011-07-31", "2012-07-31", "2013-07-31", "2014-07-31", "2015-07-31", "2016-07-31", "2017-07-31","2018-07-31", "2019-07-31"]

#Keep track of daily portoflio returns
all_portfolio_returns = pd.Series(dtype=float)

#Setting investment value
investment_value = 10000
list_of_investment_values = [10000]
list_of_selected_stocks = []

#How many stocks will be included in the efficiency frontier every year
num_stocks = 50

#Functions for efficiency frontier
def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns*weights)*365
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(365)
    return std, returns

def random_portfolios(num_stocks, num_portfolios, mean_returns, cov_matrix, risk_free_rate):
    results = np.zeros((3, num_portfolios))
    weights_record = []
    for i in range(num_portfolios):
        weights = np.random.random(num_stocks)
        weights /= np.sum(weights)
        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(weights, mean_returns, cov_matrix)
        results[0,i] = portfolio_std_dev
        results[1,i] = portfolio_return
        results[2,i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
        weights_record.append(weights)
    return results, weights_record
 
#Update investment portfolio each year. At the end of every year, the performance of each stock is evaluated and weights are assigned to each stock accordingly for the next year.
for i in range(len(years)-2):
    
    #Retrieve stocks for this year
    stocks_this_year = stocks.loc[pd.Timestamp(years[i]):pd.Timestamp(years[i+1])] 

    #Subset of stocks
    corrs = stocks_this_year.corr() 
    corr_scores = corrs.sum(axis=1)
    low_corr_stocks = []
    for _ in range(num_stocks):
        lowest_scoring_stock = corr_scores[corr_scores == min(corr_scores)].index[0]
        low_corr_stocks.append(lowest_scoring_stock)
        corr_scores.drop(lowest_scoring_stock, inplace = True)

    stocks_this_year = stocks_this_year[low_corr_stocks]

    list_of_selected_stocks.append(low_corr_stocks)

#----------------------------------------------------------------------------------
    
    #Convert prices to daily returns (log or simple)
    returns_df = stocks_this_year.pct_change().dropna()
    
    #Calculate mean returns & covariance matrix
    mean_returns = returns_df.mean()
    cov_matrix = returns_df.cov()
    
    #Define parameters for the efficient frontier function
    num_portfolios = 30000  
    risk_free_rate = 0.02

    #Generate random portfolios
    results, weights = random_portfolios(num_stocks, num_portfolios, mean_returns, cov_matrix, risk_free_rate)

    #Find portfolio and weights that correlate to the greatest Sharpe ratio
    max_sharpe_idx = np.argmax(results[2])
    weights = weights[max_sharpe_idx]

#----------------------------------------------------------------------------------

    #Retrieve stocks for next year
    stocks_next_year = stocks.loc[pd.Timestamp(years[i+1]):pd.Timestamp(years[i+2])] 
    stocks_next_year = stocks_next_year[low_corr_stocks]
    
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
    print(f"Final profit for portfolio during {years[i+1][0:4]} - {years[i+2][0:4]} :", final_profit, "%")
    #Print value of investment 
    print(f"Value of investment after July {years[i+2][0:4]}:", investment_value)

# Convert risk-free rate to daily
risk_free_daily = risk_free_rate / 365

# Calculate daily Sharpe ratio
sharpe_daily = (all_portfolio_returns - risk_free_daily).mean() / all_portfolio_returns.std()

# Annualize Sharpe
sharpe_annualized = sharpe_daily * np.sqrt(365)

print(f"Annualized Sharpe Ratio (20010-2019): {sharpe_annualized:.2f}")
    
