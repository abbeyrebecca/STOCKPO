### Portfolio with dynamic weights based on non-standard measures of return and risk

#Construct a list of strings representing the beginning of each year in datetime notation
years = ["2014-07-31", "2015-07-31", "2016-07-31", "2017-07-31",
"2018-07-31", "2019-07-31"]

#Remove all stocks with any nan values across the 5 years
stocks_no_nan = stocks.dropna(axis=1, how='any')  
 
#Update investment portfolio each year. At the end of every year, the performance of each stock is evaluated and weights are assigned to each stock accordingly for the next year.
for i in range(len(years)-2):
    
    #Retrieve stocks for this year
    stocks_this_year = stocks_no_nan.loc[pd.Timestamp(years[i]):pd.Timestamp(years[i+1])]      
    #Calculate return
    return_this_year = stocks_this_year.apply(lambda x: (x[-1]-x[0])/x[0], axis=0)    
    #Calculate risk
    risk_this_year = stocks_this_year.apply(lambda x: st.stdev(x), axis=0)
    #Calculate score
    scores_this_year = return_this_year/risk_this_year
    #Set all negative scores (which correspond to negative return) to 0 before normalising and defining weights
    scores_this_year = scores_this_year.apply(lambda x: 0 if x<0 else x)
    #Normalise scores so that their sum in equal to 1
    scores_this_year = scores_this_year.apply(lambda x: x/sum(stocks_scores))
    #These are the weights that will be used for next year's portfolio
    weights = scores_this_year

    #Retrieve stocks for next year
    stocks_next_year = stocks_no_nan.loc[pd.Timestamp(years[i+1]):pd.Timestamp(years[i+2])]  
    #Calculate return
    return_next_year = stocks_next_year.apply(lambda x: (x[-1]-x[0])/x[0], axis=0) 
    #Calculate our actual return from each stock when accounting for the weights we assigned to them
    profits = weights * return_next_year
    #Calculate our total profit
    final_profit = profits.sum() 
    #Print profit for the next year
    print(f"Final profit for portfolio during {years[i+1][0:4]} - {years[i+2][0:4]}:", final_profit)

#Notes: 
#Should develop better methods for determining risk.
#Should also make results more tangible by investing a specific amount of money at the beginning and seeing how the investment portfolio performs (i.e. how much money we make).
