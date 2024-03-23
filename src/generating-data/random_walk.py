from random import choice

class RandomWalk:
    def __init__(self, numPoints):
        self.numPoints = numPoints
        self.x = [0]
        self.y = [0]

    def fill_walk(self):

        def walk():
            return choice([1,-1]) * choice([1,2,3,4])
        
        while (len(self.x) < self.numPoints):
            # Pick random direction and distance for next X. Do same for Y
            nextX = self.x[-1] + walk()
            nextY = self.y[-1] + walk()

            # Don't append if moving nowhere
            if(nextX == 0 and nextY == 0): continue

            #Append to array
            self.x.append(nextX)
            self.y.append(nextY)
    
    def get_walk(self):
        return (self.x, self.y)