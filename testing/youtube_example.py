import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf  # Replace pandas_datareader with yfinance

# Followed along with code from https://www.youtube.com/watch?v=6-dhdMDiYWQ&t=9s

# Import stock data
def get_data(stocks, start_date, end_date):
    stockData = yf.download(stocks, start=start_date, end=end_date)['Close']  # Use yfinance's download method
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

# Create stock list
stockList = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']
stocks = [stock + '.AX' for stock in stockList]  # Add .AX for Australian stocks
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=300)

# Quick test
meanReturns, covMatrix = get_data(stocks, start_date, end_date)

print(meanReturns)