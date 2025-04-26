
# Now lets do static relative weights, change the weightages of each stock every 3 months to maintain the initial weightages of each stock.
# Assume that `prices` is your DataFrame containing only the daily prices of each stock for the testing year (2018-08-01 to 2019-07-01).


initial_weights1 = [0.115, 0.102, 0.100, 0.087, 0.087, 0.086, 0.085, 0.083, 0.082, 0.082] # These are the weights of each stock in the portfolio according to their individual Sharpe ratios.

def calculate_portfolio_profit(prices, initial_weights):
    initial_weights = np.array(initial_weights)

    # Rebalance dates every 3 months
    rebalance_dates = ['2018-11-01', '2019-02-01', '2019-05-01',
               '2019-08-01']

    # Track portfolio value over time
    portfolio_value = pd.Series(index=prices.index, dtype=float)
    initial_money = 10000  
    # The starting prices of each stock 
    start_prices = prices.iloc[0]
    dollar_allocation = initial_money * initial_weights 
    
    # Holdings is the number of shares you have of each stock
    holdings = dollar_allocation / start_prices
    
    # Calculate how much money is in your portfolio on the day right before rebalancing it for the first time.
    current_money = holdings * prices.loc['2018-11-01']

    for i, date in enumerate(rebalance_dates):
        # Define the rebalancing period
        start_date = date
        end_date = rebalance_dates[i+1] if i+1 < len(rebalance_dates) else prices.index[-1]
        period_prices = prices.loc[start_date:end_date]
        
        if period_prices.empty:
            continue
        
        # Get prices at the start of the period
        start_prices = period_prices.iloc[0]

        # Rebalance: Calculate how many shares to buy for each stock
        dollar_allocation = current_money * initial_weights
        holdings = dollar_allocation / start_prices

        # Calculate portfolio value for the period
        for day in period_prices.index:
            day_prices = prices.loc[day]
            portfolio_value[day] = np.sum(holdings * day_prices)

        # Update current value for the next rebalance
        current_money = portfolio_value.loc[period_prices.index[-1]]

    # Profit is final portfolio value - initial capital
    final_value = portfolio_value.dropna().iloc[-1]
    profit = final_value - initial_money

    return (profit, portfolio_value)

port_valueprofit = calculate_portfolio_profit(stock_last_1, initial_weights1)

print(port_valueprofit)

# The profit you get using static relative weights is -9262 dollars, much worse performance than using static normal weights with a loss of only 147 dollars.

