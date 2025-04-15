# The Purpose of This README.md

This README.md file is mostly for personal notes I can refer to while discovering how a Monte Carlo simulation works. It's more of a lesson log to hammer in what I've learned rather than being purely a guide for running this code. Big thanks to the book "Fooled by Randomness", by Nassim Nicholas Taleb, for inspiring this super interesting project. There are so many valuable concepts in this book that I feel this is the best way to fully digest them. I also might be stealing his rhetoric here and there, so I apologize if I occasionally sound pretentious.

# The Purpose of This Project

HindSite is meant to give me new insights into my Robinhood account and the trades I've made using a Monte Carlo simulation. I started this project in February of 2025, which has been a very uncertain time for U.S. markets. This uncertainty, in combination with Taleb's "Fooled by Randomness", has made me worry about the resilliance of my portfolio and my understanding of risk. I've taken a very organic approach to investing so far, and my intuition seems to be working for now. However, I've finally decided to blend some statistics into the mix, as I believe the best and most sustainable way to invest is through organic thought mixed with statistical analysis.

# An Introduction To The Monte Carlo Simulation

We'll start with [this lecture](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/lecture-6-monte-carlo-simulation/) from MIT Open Course Ware. Thank you Professor Guttag for the free lesson!

## Inferential Statistics

> **A Monte Carlo simulation is "a method of estimating the value of an unknown quantity using the principles of inferential statistics"**
>
> - **Population**: A set of examples
> - **Sample**: A proper subset of a population
> - A random sample tends to exhibit the same properties as the population from which it is drawn.

These are things we already know, but they are important to keep in mind.

Guttag then references the classic example of a coin flip to illustrate the idea. Ironically, this is something that Taleb thinks is a poor approach to understanding the true notions behind the simulation.

Anyway, it's as simple as it gets: the more you flip the coin, the more the sample population tends to show that the coin flip has 50/50 odds.

### Confidence in our estimate depends on two things:

> - Size of the sample
> - Variance of the sample
> - As the variance grows, we need larger samples to have the same degree of confidence

Again, all very simple and familiar concepts. No need for further elaboration.

## Roulette and OOP

This example allows us to compare simulation results to actual probabilities. Taleb likes Russian Roulette more in the context of investors taking extreme losses, but the idea remains the same.

Thankfully, this course is taught in Python. Unfortunately, it looks like I'm finally going to have to actually learn OOP, rather than just understand the basic idea.

### Object-Oriented Programming - Classes

> - When you create a class, you're creating a blueprint for objects. Each object needs
>   its own separate copy of the data. That's what "self" helps with.
> - In other words, "self" is simply a reference to "this specific object instance"
>   It's the way Python lets an object access its own data and methods.
> - In summary, classes are used to calculate different data using the same calculations in a compartmentalized manner.

### Object-Oriented Programming - Basic Structure

> - You define methods inside a class
> - You create an instance of that class
> - You can then call those methods on the instance

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

# Starting Simple - First Test of the Simulation

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

## Define weights for the portfolio
Now we define the weights. In this case, we're just gonna use random numbers for these values to keep the simplicity.
```python
weights = np.random.random(len(meanReturns)) # We'll randonly generate weights for now (ranges from 0 to 1)
weights /= np.sum(weights) # Normalize the weights to sum to 1 by dividing them by the sum of the weights

print(f'Weights: {weights}') # Testing the weights
```

Finally... we can actually start playing around with the Monte Carlo Simulation.