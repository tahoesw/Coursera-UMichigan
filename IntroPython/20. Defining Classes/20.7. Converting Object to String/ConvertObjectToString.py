#2 Point
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

p = Point(7, 6)
q = Point(1, 1)
print("Point p:", p)
print("Point q:", q)

print()
#3 Cereal
class Cereal:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initName, initBrand, initFiber):

        self.name = initName
        self.brand = initBrand
        self.fiber = initFiber

    def getName(self):
        return self.name

    def getBrand(self):
        return self.brand

    def getFiber(self):
        return self.fiber

    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,
                                       self.brand, self.fiber)

c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)
print(c1)
print(c2)
