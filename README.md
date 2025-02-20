# The Preliminary Purpose of This README.md File

As of now, this README.md file is for personal notes I can refer to while discovering how a Monte Carlo simulation works. Big thanks to the book "Fooled by Randomness", by Nassim Nicholas Taleb, for inspiring this super interesting project.

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

## Roulette

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
for numSpins in (100, 1000000):
    for i in range(3):
        playRoulette(game, numSpins, 2, 1, True)
```

### What We Learned
