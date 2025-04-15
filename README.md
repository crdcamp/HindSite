# The Purpose of This README

This README file is mostly for personal notes I can refer to while discovering how a Monte Carlo simulation works. It's more of a lesson log to hammer in what I've learned rather than being purely a guide for running this code. Big thanks to the book "Fooled by Randomness", by Nassim Nicholas Taleb, for inspiring this super interesting project. There are so many valuable concepts in this book that I feel this is the best way to fully digest them. I also might be stealing his rhetoric here and there, so I apologize if I occasionally sound pretentious.

# The Purpose of This Project

HindSite is meant to give me new insights into my Robinhood account and the trades I've made using a Monte Carlo simulation. I started this project in February of 2025, which has been a very uncertain time for U.S. markets. This uncertainty, in combination with Taleb's "Fooled by Randomness", has made me worry about the resilliance of my portfolio and my understanding of risk. I've taken a very organic approach to investing so far while intuition seems to be working for now. However, I've finally decided to blend some statistics into the mix, as I believe the best and most sustainable way to invest is through organic thought mixed with statistical analysis. I'm almost certain my portfolio is highly susceptible to a financial shock, so now it's time to address that concern.

# An Introduction To The Monte Carlo Simulation

We'll start with [this lecture](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/lecture-6-monte-carlo-simulation/) from MIT Open Course Ware. Thank you Professor Guttag for the free lesson!

## Inferential Statistics

**A Monte Carlo simulation is "a method of estimating the value of an unknown quantity using the principles of inferential statistics"**
* **Population**: A set of examples
* **Sample**: A proper subset of a population
* A random sample tends to exhibit the same properties as the population from which it is drawn.

These are things we already know, but they are important to keep in mind.

Guttag then references the classic example of a coin flip to illustrate the idea. Ironically, this is something that Taleb thinks is a poor approach to understanding the true notions behind the simulation.

Anyway, it's as simple as it gets: the more you flip the coin, the more the sample population tends to show that the coin flip has 50/50 odds.

### Confidence in our estimate depends on two things:

* Size of the sample
* Variance of the sample
* As the variance grows, we need larger samples to have the same degree of confidence

Again, all very simple and familiar concepts. No need for further elaboration.

## Roulette and OOP

This example allows us to compare simulation results to actual probabilities. Taleb likes Russian Roulette more in the context of investors taking extreme losses, but the idea remains the same.

Thankfully, this course is taught in Python. Unfortunately, it looks like I'm finally going to have to actually learn OOP, rather than just understand the basic idea.

### Object-Oriented Programming - Classes

* When you create a class, you're creating a blueprint for objects. Each object needs its own separate copy of the data. That's what "self" helps with.
* In other words, "self" is simply a reference to "this specific object instance"
* It's the way Python lets an object access its own data and methods.
* In summary, classes are used to calculate different data using the same calculations in a compartmentalized manner.

### Object-Oriented Programming - Basic Structure

* You define methods inside a class
* You create an instance of that class
* You can then call those methods on the instance

### Guttag's Roulette Simulation

```python
import random

class FairRoulette(): # This is the blueprint for our roulette game
# Guttag named it "FairRoulette" because it's set up so your expected value is 0
# It isn't a negative or positive sum game

    def __init__(self): # This runs when we create a new roulette game
        self.pockets = [] # self.pockets creates the variable "pockets" that belongs to a specific roulette wheel
        for i in range(1,37):
            self.pockets.append(i)
        self.ball = None # Initially we don't know where the ball is so self.ball = None
        self.pocketOdds = len(self.pockets) - 1 # Tells you what your odds are. If you win, you get $36

    def spin(self):
        self.ball = random.choice(self.pockets) # Simplified to not allow bets on colors

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds # Player wins
        else:
            return - amt # Player loses

    def __str__(self): # How our roulette wheel describes itself
        return 'Fair Roulette'

# Now we make the game playable
def playRoulette(game, numSpins, pocket, bet, toPrint):
    totPocket = 0

    for i in range(numSpins):
        game.spin()
        totPocket += game.betPocket(pocket, bet) # Will return 0 if lost, and 35 if won

    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting', pocket, '=',\
                str(100*totPocket/numSpins) + '%\n')

    return (totPocket/numSpins)

# Finally, run the simulation
random.seed(0)
game = FairRoulette()
for numSpins in (100, 1000000): # We're testing what happens when you spin 100 times vs. 1000000 times
    for i in range(3):
        playRoulette(game, numSpins, 2, 1, True)
```

### Roulette Simulation Results and What We Learned

Here are the results of the simulation:

```terminal
100 spins of Fair Roulette
Expected return betting 2 = -100.0%

100 spins of Fair Roulette
Expected return betting 2 = 44.0%

100 spins of Fair Roulette
Expected return betting 2 = -28.0%

1000000 spins of Fair Roulette
Expected return betting 2 = -0.046%

1000000 spins of Fair Roulette
Expected return betting 2 = 0.602%

1000000 spins of Fair Roulette
Expected return betting 2 = 0.7964%
```

And here's what we learned:

- For 100 spins, the return is **highly variable**
- However, for 1,000,000 spins, there is much less variance. Still not 0, but evidently closer to 0, and notably the results are closer together (less variance).
- The more you spin (the larger the population), the less the variance. The casino, of course, likes the odds of the larger sample size.
- The more spins we do, the closer to 0 we get, and the less variance there is.

This is that good old concept of the **Law of Large Numbers**. While this still isn't any sort of breakthrough or epiphany, it does strongly tie into Taleb's points.

### The Law of Large Numbers

"In repeated independent tests with the same actual probability _p_ of a particular outcome in each test, the chance that the fraction of times that outcome occurs differs from _p_ converges to 0 as the number of trials goes to infinity."

Again, another pretty simple and well known concept, but the roulette code was fun to follow along with anyway. It's also time to grow up and start using OOP a lot more. This will greatly improve my code.

### The Gambler's Fallacy and it's Ties to Taleb

The lecture I've been referencing also brings up some notable points that remind me of Taleb's book. As Professor Guttag put it, "People somehow believe that if deviations from the expectation occur, they'll be evened out in the future. This is simply not true." Taleb displayed this with stories of investors "blowing up" over foreign currencies in the 90s. The one guy in particular (I forget what Taleb called him) would keep dollar cost averaging into the Ruple thinking that, eventually, his previously successful strategy would show results again. He was so caught up in the affirmations of his circle of economists that he ran into a statistical certainty of failure (I'm not sure if Taleb would frown at the "statistical certainty" part of that conclusion, but the idea remains the same still). Never marry yourself to an asset, or (more importantly for the application of this project) a trading strategy. **No economic regime is permanent.**

In the end, this particular investor was "lucky" in the sense that he was **randomly** in the right place at the right time. This is why his strategy worked so well, that is, until he "blew up". If you play Russian roulette enough times, no matter how many chambers the revolver may have, you will eventually lose. This is why we're learning about the Monte Carlo simulation. We must be aware of all possible outcomes, not blinded by the strategy that currently works.

### A Common Confusion - The Gambler's Fallacy vs. Regression to the Mean

Following the Gambler's Fallacy, Guttag makes an important distinction concerning Regression to the Mean:

"If somebody's parents are both taller than average, it's likely that the child will be shorter than the parents."

The same logic applies invesely. Essentially, when following an extreme event, the next random event is likely to be less extreme (I wonder what Taleb thinks of this). I'll avoid indulging in this idea too much, as this concept becomes foggy and unreliable without a given timeframe (long term vs. short term, and what the distinction between the two even really is). It's also important to keep in mind that, as Taleb said, **there is a big difference between a game and the real world**. This is also why he said he doesn't like competitive people. A competitve mindset treats the market like a game rather than the convoluted and random mess that it really is. This also might imply that the time series of my data and what I compare it to is going to be very tricky (and probably somewhat arbitrary) to implement. Moreoever, genetic inherence doesn't really involve the consideration of time in this example.

I will need to revisit this later when the project's parameters are more clear. Let's avoid more confusion and continue with Guttag and the roulette example.

### Roulette - Regression to the Mean

Again, following an extreme random event, the next random event is likely to be less extreme. If you spin a fair roulette wheel 10 times and get 100% reds, that is an extreme event (1 in 1024 chance).

The Gambler's Fallacy says that if you spin another 10 times it should "even out". You should get less than 10 blacks to make up for the reds.

Regression to the Mean says that its likely that in the next 10 spins, you will get around 5 reds (a less extreme random event). The statistically expected number of reds is around 5, while the Gambler's Fallacy expects less than 10.

So, if you look at the average of the 20 spins, it will be closer to the expected mean of 50% reds than to the 100% of the first 10 spins. This is reillustrating the concept from earlier, where if you spin the roulette wheel a million times the reward converges to $0.

**The more samples you take, the more likely you will regress to the mean**. The result isn't _evening out_, it is _regressing_ towards the statistically expected result. However, let's not marry ourselves to this idea before our understanding is fully grounded. Roulette is a game where the rules stay the same. The market is not and has way less static probabilities. People have lost their fortune on events they deemed far less likely than getting 10 reds in a row. Taleb hates it when people omit outliers for a reason.

# Starting Simple - First Monte Carlo Test

Now it's time to see what we can do with a simple test. Thanks to [this video](https://www.youtube.com/watch?v=6-dhdMDiYWQ&t=9s) by QuantPy, we have a good place to start. We begin by simply finding the mean returns of some Austrailian stocks.

## Finding Stock Mean Returns

```python
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
stocks = [stock + '.AX' for stock in stockList]  # Add .AX for Australian stocks. This will be changed later
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=300)

# Quick test
meanReturns, covMatrix = get_data(stocks, start_date, end_date)

print(meanReturns)
```
This (obviously) finds the stock mean returns. We begin by gathering the stock data (close prices), then calculating the daily percentage changes. The daily percent changes are then used to find the average daily return for each stock over a specific period.

The covariance matrix (```covMatrix```) then captures how the returns of different stocks move in relation to each other. 

As a review, a covariance matric captures the relationships between multiple variables. You can intepret a covariance matrix by understanding that diagonal elements represent the variance of each stock, while off-diagonal elements represent the covariance between stocks i and j. More on that later.

## Define weights for the portfolio
Now we define the weights. In this case, we're just gonna use random numbers for these values to keep the simplicity.
```python
weights = np.random.random(len(meanReturns)) # We'll randonly generate weights for now (ranges from 0 to 1)
weights /= np.sum(weights) # Normalize the weights to sum to 1 by dividing them by the sum of the weights

print(f'Weights: {weights}') # Testing the weights
```

The random weights don't add up to 1, so we normalize by dividing the number of weights by their sum. Finally... we can actually start playing around with the Monte Carlo Simulation.

## Setting Up the Simulation
There's a lot to unpack here and a lot of learning to reflect on. We begin by determining the number of simulations and the time frame in days.
```python
# Monte Carlo Method
mc_sims = 100 # Number of simulations. We'll figure out what this means more precisely later
T = 100 # Timeframe in days
```
The number of simulations determines the following:
* The precision and reliability of the output distributions. When you run more simulations, you reduce the impact of random variation or outliers.
* With more simulations, you can more precisely estimate the likelihood of different outcomes, **especially rare events** (Taleb liked that).
* More simulations typically narrow confidence intervals and provide better estimates of potential outcomes.

After we determine the number of simulations and the timeframe, we define empty arrays to store and retrieve information. 

```python
# Define some empty arrays that we're gonna store and retrieve information from 
meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns) # Mean matrix. Need to look into what .full does
meanM = meanM.T # Transpose the mean matrix
```
The variable ```meanM``` is the mean matrix. This is essentially duplicating the mean returns 100 times (once for each day in the timeframe). The np.full() function creates an array of the specified shape and fills it with the value provided.

```shape=(T, len(weights))``` is specifying that you want to create a 2D array with 100 T rows and 6 weight columns. One column for each stock.

The transposition ensures that when you perform this calculation, the dimensions match properly for matrix operations. When you transpose the matrix with ```meanM = meanM.T```, you are flipping a matrix over its diagonal and switching its rows and columns. Keep in mind that ```.T``` is a property, not a method, that returns the transposed version of the matrix. The diagonal remains in the same position, but all other elements change their position.

Before the transposition, ```meanM``` is a matric with shape (100, 6). After, it becomes (6, 100).

This aligns everything correctly in order for the calculation to work properly.

```python
portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0) # Array that we're storing the matrix in. Fill value = 0.0 to allow for float values

initialPortfolioValue = 10000 # Initial portfolio value. This is the value of the portfolio at time 0
```
```python
for m in range(0, mc_sims):
    # MC loops
    Z =- np.random.normal(size=(T, len(weights))) # Generate a random normal distribution
    L =  np.linalg.cholesky(covMatrix) # Cholesky decomposition. This finds the value for that "lower triangle"
    dailyReturns = meanM + np.inner(L, Z) # Inner product of the mean matrix and the lower triangle
    portfolio_sims[:, m] = np.cumprod(np.inner(weights, dailyReturns.T)+1) * initialPortfolioValue # Cumulative product of the daily returns and the initial portfolio value

plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value ($)')
plt.xlabel('Days')
plt.title('Monte Carlo Simulation of Portfolio Value')
plt.show()
```

We use the **Cholesky decomposition** ```L``` to determine the Lower Triangular matrix. 

## Cholesky Decomposition - What Is It and Would Taleb Approve?

I couldn't help but notice that the ```Z``` variable uses a normal distribution. In the context of the stock market, Taleb HATES normal distributions. This is because, according to him, a normal distribution cannot be used on things like the stock market. He states that the market belongs to "Extremistan"; a domain where the cumulative magnitude of an outlier scales completely differently than those of "Mediocristan". Mediocristan is a domain where variables are well-behaved, follow normal distributions, and extreme outcomes are almost impossible.

* **Extremistan** - A domain where events have systematic effects. One event can affect more than one person, and the results can compound.
* **Mediocristan** - A domain where the individual is affected without correlation to the collective.

I'm a firm believer in Taleb's take on this. While I try to not blindly agree with everything he says, he is almost certainly correct about this central point in his book "The Black Swan". In the context of market/risk assessment, the normal distribution must die!

Before I get too deep into this preconcieved bias, let's do some research into the Cholesky Decompostion and make some educated conclusions.

### Cholesky Decomposition - The Concepts Behind It

We'll start with [this resource](https://www.statlect.com/matrix-algebra/Cholesky-decomposition) to get an idea of what's happening here.

"A square matrix is said to have a Cholesky decomposition if it can be written as the product of a lower triangular matrix and its transpose (conjugate transpose in the complex case); the lower triangular matrix is required to have strictly positive real entries on its main diagonal."

Let's start with the completeley unfamiliar part; the **triangular matrix**.

#### Triangular Matrices
To begin with, a square matrix is a matrix that has an equal number of rows and columns. Super simple stuff.

Meanwhile, accoring to [CueMath](https://www.cuemath.com/algebra/triangular-matrix/):

"A triangular matrix is a special kind of square matrix in the set of matrices. There are two types of triangular matrices: lower triangular matrix and upper triangular matrix."
* "A square matrix is said to be a lower triangular matrix if all the elements above its main diagonal are zero."
* "A square matrix is said to be an upper triangular matrix if all the elements below the main diagonal are zero."

Let's create a new file for testing to display the lower triangle. The Cholesky Decomposition / lower triangle in quantpy_youtube_example.py is found right here.

```python
L =  np.linalg.cholesky(covMatrix)
```

After creating a new file called quantpy_youtube_example_testing.py (just in case we gotta mess around with the code some more), we'll edit the code to print this example from the above line.

```
[[ 0.01471784  0.          0.          0.          0.          0.        ]
 [ 0.00275857  0.01353353  0.          0.          0.          0.        ]
 [ 0.00297616  0.01048601  0.00897381  0.          0.          0.        ]
 [ 0.00752823  0.00615682  0.00060933  0.01426829  0.          0.        ]
 [ 0.00022687  0.00177266 -0.0005684   0.00170653  0.00790305  0.        ]
 [ 0.00347986  0.00973975  0.00349588  0.00047145  0.00093471  0.00686941]]
```

Understanding this might be more easy than I thought. A lower triangular matrix is when all elements above its main diagonal are zero, and this clearly fits the definition. 

We use the lower triangular matrix in the simulation for the following reasons:
* **Factorization of the Covariance Matrix**: The covariance matrix captures how assets move together, but we can't use it to generate random returns. The lower triangular matrix is a factorization that, when multiplied by itself transposed, perfectly reproduces the original covariance matrix.
* **Sequential Dependency Structure**: The lower triangular structure creates a specific pattern of dependencies. Each row only depends only on previous rows, which matches the way financial correlations often work in market models.
* **Mathematical Consistency**: The lower triangular matrix ensures that the resulting simulated returns have exactly the statistical properties defined by the covariance matrix.

We can then use the lower triangular matrix to **transform independent random numbers into correlated random numbers than maintain the exact relationships defined in the covariance matrix**.

While I don't have an understanding of the math behind this, the concept of generating numbers randomly based on the correlations certainly makes sense. Diving into the formulas is likely a waste of time at this point, as I highly doubt we will be using a Cholesky Decomposition in the final calculations.

Let's move on to how the Cholesky Decomposition works. Then we can have a better understanding of how to replace it.

#### Verifying PyQuant's Cholesky Decomposition
To reiterate from the [Cholesky Decomposition source](https://www.statlect.com/matrix-algebra/Cholesky-decomposition): 

"A square matrix is said to have a Cholesky decomposition if it can be written as the **product of a lower triangular matrix and its transpose** (conjugate transpose in the complex case); the **lower triangular matrix is required to have strictly positive real entries on its main diagonal**."

This definition makes more sense now. Let's also revisit the example from earlier.


```
[[ 0.01471784  0.          0.          0.          0.          0.        ]
 [ 0.00275857  0.01353353  0.          0.          0.          0.        ]
 [ 0.00297616  0.01048601  0.00897381  0.          0.          0.        ]
 [ 0.00752823  0.00615682  0.00060933  0.01426829  0.          0.        ]
 [ 0.00022687  0.00177266 -0.0005684   0.00170653  0.00790305  0.        ]
 [ 0.00347986  0.00973975  0.00349588  0.00047145  0.00093471  0.00686941]]
```

The [main diagonal](https://www.sciencedirect.com/topics/mathematics/diagonal-of-a-matrix#:~:text=The%20main%20diagonal%20of%20a,element%20to%20the%20lower%20right.) of a matrix refers to the elements where the row and column numbers are the same. Given this definition, You can easily see that the lower triangular matrix has only positive real entries on its main diagonal.

As for the "product of a lower triangular matrix and its transpose", we will do some more testing. I've changed the bottom code in quantpy_youtube_example_testing to this.

```python
for m in range(0, mc_sims):
    # MC loops
    # We use the Cholesky decomposition to determine the Lower Triangular matrix
    # He mentions "normal distribution" in relation to this. I dont think Taleb would approve, BUT we're keeping it simple for now
    Z = np.random.normal(size=(T, len(weights))) # Generate a random normal distribution
    L =  np.linalg.cholesky(covMatrix) # Cholesky decomposition. This finds the value for that "lower triangle"
    dailyReturns = meanM + np.inner(L, Z) # Inner product of the mean matrix and the lower triangle
    portfolio_sims[:, m] = np.cumprod(np.inner(weights, dailyReturns.T)+1) * initialPortfolioValue # Cumulative product of the daily returns and the initial portfolio value

    # Testing Section: Determine if the Cholesky decomposition can be written as the product of the lower triangular matrix and its transpose
    L_LT_product= np.matmul(L, L.T) # Product of L and its transpose
    is_valid_decomposition = np.allclose(L_LT_product, covMatrix) # Check if the product is equal to the covariance matrix
```
This checks to see if the original covariance matrix equals the product of the Cholesky Decomposition and its transpose. The result returned a lovely ```True``` statement. As far as I can tell, the YouTube example was done correctly. Now let's understand the whole point of a Cholesky Decomposition so we can explore alternatives.

#### How Dependant on the Normal Distribution is a Cholesky Decomposition?

As we've already discovered, the Cholesky Decomposition is used for simulating systems with multiple correlated variables. That's interesting and all, but why does it use the dreaded normal distibution? These Gaussian concepts are not welcome in my analysis! Do you hear me, Taleb!?

Let's take another look at when the code creates a random normal distribution, applies the Cholesky Decomposition, and then does the rest of the magic.

```python
Z = np.random.normal(size=(T, len(weights))) # Generate a random normal distribution
L =  np.linalg.cholesky(covMatrix) # Cholesky decomposition. This finds the value for that "lower triangle"
dailyReturns = meanM + np.inner(L, Z) # Inner product of the mean matrix and the lower triangle
portfolio_sims[:, m] = np.cumprod(np.inner(weights, dailyReturns.T)+1) * initialPortfolioValue # Cumulative product of the daily returns and the initial portfolio value
```

Clearly, the calculations are completely reliant on Gaussian concepts. The entire Cholesky part is completely dependant on the randomly generates distribution assigned to ```Z```. The result of the simulation is founded on a basic Gaussian concept. This is all I need to know. Now it's time to take some of Taleb's advice.

# The Power Law and Talebs Lover Benoit Mandelbrot

As much as I want to get ahead of myself and start immediately applying Talebs ideas to a Monte Carlo simulation, let's get some foundational understanding first.
