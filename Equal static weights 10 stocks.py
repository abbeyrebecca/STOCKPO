fig, ax = plt.subplots()

all_investments = []
all_stocks = []

for i in range(10):
    stocks = pd.read_csv('adjprice.csv')
    stocks.set_index(pd.to_datetime(stocks["Date"], format='%Y%m%d'), inplace=True)
    stocks.drop(columns=["Date"], inplace=True)
    stocks.dropna(axis=1, how='any', inplace=True)  
    stocks = stocks.sample(50, axis=1)
    
    
    corrs = stocks.corr() 
    corr_scores = corrs.sum(axis=1)
    low_corr_stocks = []
    for i in range(10):
        lowest_scoring_stock = corr_scores[corr_scores == min(corr_scores)].index[0]
        low_corr_stocks.append(lowest_scoring_stock)
        corr_scores.drop(lowest_scoring_stock, inplace = True)
    
    
    #Construct a list of strings representing the beginning of each year in datetime notation
    years = ["2010-07-31", "2011-07-31", "2012-07-31", "2013-07-31", "2014-07-31", "2015-07-31", "2016-07-31", "2017-07-31","2018-07-31", "2019-07-31"]
    
    stocks_no_nan = stocks.loc[:,low_corr_stocks]
    all_stocks.append(low_corr_stocks)

    #Keep track of daily portoflio returns
    all_portfolio_returns = pd.Series(dtype=float)

    #Set risk-free rate
    risk_free_rate = 0.02
    
    investment_value = 10000
    
    list_of_investment_values = [10000]
    
    weights = [1/stocks_no_nan.shape[1]]*stocks_no_nan.shape[1]
    
    #At the end of every year, the performance of each stock is evaluated.
    for i in range(len(years)-1):
    
        #Retrieve stocks for next year
        stocks_next_year = stocks_no_nan.loc[pd.Timestamp(years[i]):pd.Timestamp(years[i+1])]  
        #Calculate return
        daily_returns_next_year = stocks_next_year.pct_change().dropna()
        portfolio_returns = daily_returns_next_year @ weights
        final_profit = (portfolio_returns + 1).prod() - 1
        #Add to daily portfolio return list
        all_portfolio_returns = pd.concat([all_portfolio_returns, portfolio_returns])
        #Update investment value
        investment_value = investment_value*(1+final_profit)
        list_of_investment_values.append(investment_value)

    # Convert risk-free rate to daily
    risk_free_daily = risk_free_rate / 365
    
    # Calculate daily Sharpe ratio
    sharpe_daily = (all_portfolio_returns - risk_free_daily).mean() / all_portfolio_returns.std()
    
    # Annualize Sharpe
    sharpe_annualized = sharpe_daily * np.sqrt(365)
    
    print(f"Annualized Sharpe Ratio (2010-2019): {sharpe_annualized:.2f}")

    years = np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])

    all_investments.append(list_of_investment_values)
    
    ax.plot(years, list_of_investment_values)
    
ax.set(xlabel='Year', ylabel='Investment value', title='Investment value over time')
ax.grid()
plt.show()
