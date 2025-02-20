import random

class FairRoulette(): # This is the blueprint for our roulette game

    def __init__(self): # This runs when we create a new roulette game
        self.pockets = [] # self.pockets creates the variable "pockets" that belongs to a specific roulette wheel
        for i in range(1,37):
            self.pockets.append(i)
        self.ball = None
        self.pocketOdds = len(self.pockets) - 1 # How much we pay out if someone wins

    def spin(self):
        self.ball = random.choice(self.pockets)

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds # Player wins
        else:
            return - amt # Player loses

    def __str__(self): # How our roulette wheel describes itself
        return 'Fair Roulette'

# Now we create an instance of the game
wheel = FairRoulette()
wheel.spin()
result = wheel.betPocket(7,10) # Bet $10 on pocket 7
print(result) # Then be reminded why I don't gamble