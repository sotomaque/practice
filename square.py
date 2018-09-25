class Square:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        length = math.fabs(self.a.x - self.b.x)
        if length == 0:
          length = math.fabs(self.a.x - self.c.x)
          if len == 0:
            length = math.fabs(self.a.x - self.d.x)
        width = math.fabs(self.a.y - self.b.y)
        if width == 0:
          width = math.fabs(self.a.y - self.c.y)
          if len == 0:
            width = math.fabs(self.a.y - self.d.y)
        area = length * width
      	return area

    def setArea(self):
    	a = self.area()
    	self.area = a

    def __str__(self):
    	return 'square([{0},{1}, {2}, {3}])'.format(self.a, self.b, self.c, self.c)