from random import randint

class Die:
    def __init__(self, numSides=6):
        # Edge conditions
        if(numSides < 1): raise ValueError('Die must have at least one side')
        if(type(numSides) == bool): raise TypeError('Die class does not accept booleans')
        numSides = int(numSides) # Cast numSides into an integer

        self.numSides = numSides

    def roll(self):
        return randint(1, self.numSides)