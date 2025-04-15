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

print(f'Mean Returns: {meanReturns}')


# Define weights for the portfolio
weights = np.random.random(len(meanReturns)) # We'll randonly generate weights for now (ranges from 0 to 1)
weights /= np.sum(weights) # Normalize the weights to sum to 1 by dividing them by the sum of the weights

print(f'Weights: {weights}') # Testing the weights

# Now we can dive into the Monte Carlo simulation

# Monte Carlo Method
mc_sims = 100 # Number of simulations. We'll figure out what this means more precisely later
T = 100 # Timeframe in days

# Define some empty arrays that we're gonna store and retrieve information from 
meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns) # Mean matrix
meanM = meanM.T # Transpose the mean matrix

portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0) # Array that we're storing the matrix in. Fill value = 0.0 to allow for float values

initialPortfolioValue = 10000 # Initial portfolio value. This is the value of the portfolio at time 0

for m in range(0, mc_sims):
    # MC loops
    # We use the Cholesky decomposition to determine the Lower Triangular matrix
    # He mentions "normal distribution" in relation to this. I dont think Taleb would approve, BUT we're keeping it simple for now
    Z =- np.random.normal(size=(T, len(weights))) # Generate a random normal distribution
    L =  np.linalg.cholesky(covMatrix) # Cholesky decomposition. This finds the value for that "lower triangle"
    dailyReturns = meanM + np.inner(L, Z) # Inner product of the mean matrix and the lower triangle
    portfolio_sims[:, m] = np.cumprod(np.inner(weights, dailyReturns.T)+1) * initialPortfolioValue # Cumulative product of the daily returns and the initial portfolio value

plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value ($)')
plt.xlabel('Days')
plt.title('Monte Carlo Simulation of Portfolio Value')
plt.show()