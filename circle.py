class circle:
    def __init__(self,radius) :
        self._radius = radius
        self._diameter = 2 * radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, r):
        self._radius = r
        self._diameter = 2 * r
    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, d):
        self._diameter = d
        self._radius = int(d / 2)
    def __str__(self):
        return "반지름 : {}, 지름 : {}".format(self.radius, self.diameter)    
circle1 = circle(3)

print(circle1)

circle1.radius = 2

print(circle1)

circle1.diameter = 10

print(circle1)