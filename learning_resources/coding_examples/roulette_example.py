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