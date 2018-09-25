import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pythagreanDistance(self):
		distance = float(math.sqrt((self.x)**2 + (self.y)**2))
		return distance

    def displayDistanceToOrigin(self):
    	d = self.pythagreanDistance()
        print ("Distance to Origin :", d )

    def getDistanceToOrigin(self):
    	d = self.pythagreanDistance()
    	return d

    def __str__(self):
    	return 'point([{0},{1}])'.format(self.x, self.y)

