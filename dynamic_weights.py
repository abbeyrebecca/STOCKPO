#Construct a list of strings representing the beginning of each year in datetime notation
years = ["1994-01-01", "1995-01-01", "1996-01-01", "1997-01-01", "1998-01-01", "1999-01-01",
"2000-01-01", "2001-01-01", "2002-01-01", "2003-01-01", "2004-01-01", "2005-01-01",
"2006-01-01", "2007-01-01", "2008-01-01", "2009-01-01", "2010-01-01", "2011-01-01",
"2012-01-01", "2013-01-01", "2014-01-01", "2015-01-01", "2016-01-01", "2017-01-01",
"2018-01-01", "2019-01-01"]
 
#Update investment portfolio each year. At the end of every year, the performance of each stock is evaluated and weights are assigned to each stock accordingly for the next year.
for i in range(len(years)-2):
    
    #Retrieve stocks for this year
    stocks_this_year = stocks.loc[pd.Timestamp(years[i]):pd.Timestamp(years[i+1])]
    #Drop all stocks which leave the S+P 500 at any time during the year
    stocks_this_year = stocks_this_year.dropna(axis=1, how='any')    
    #Calculate return
    stocks_return = stocks_this_year.apply(lambda x: x[-1]-x[0], axis=0)    
    #Calculate risk
    stocks_risk = stocks_this_year.apply(lambda x: st.stdev(x), axis=0)
    #Calculate score
    stocks_scores = stocks_return/stocks_risk
    #Set all negative scores (which correspond to negative return) to 0 before normalising and defining weights
    stocks_scores = stocks_scores.apply(lambda x: 0 if x<0 else x)
    #Normalise scores so that their sum in equal to 1
    stocks_scores = stocks_scores.apply(lambda x: x/sum(stocks_scores))
    #These are the weights that will be used for next year's portfolio
    weights = stocks_scores

    #Retrieve stocks for next year
    stocks_next_year = stocks.loc[pd.Timestamp(years[i+1]):pd.Timestamp(years[i+2])]  
    #Drop all stocks which leave the S+P 500 at any time during the year
    stocks_next_year = stocks_next_year.dropna(axis=1, how='any') 
    #Calculate return. This may return some nan values, since not all stocks who had no nan values in one year will have again no nan values in the next year
    profits = stocks_next_year.apply(lambda x: x[-1]-x[0], axis=0) 
    #Calculate our actual return from each stock when accounting for the weights we assigned to them
    weighted_profits = weights * profits
    #Calculate our total profit
    final_profit = weighted_profits.sum() #Ignores nan values
    #Print profit for the next year
    print(f"{years[i+1][0:4]} final profit:", final_profit)

#Notes: 
#Should develop better methods for determining risk.
#Should also make results more tangible by investing a specific amount of money at the beginning and seeing how the investment portfolio performs (i.e. how much money we make).
    
