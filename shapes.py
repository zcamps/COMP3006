#Zackary Campbell
#COMP3006 project 5
#This file creates a shape class and then creates sub classes of that class that allow you to do
#essential shape functions (calculate area, perimeter, etc.)

import math



class shape:

    def __init__(self, numSides):
        self.numSides = numSides

    def area(self):
        return 'specify a shape'

    def perimeter(self):
        return 'specify a shape'

class ellipse(shape):
    def __init__(self, majRad, minRad):
        super(ellipse, self).__init__(1)
        self.majRad = majRad
        self.minRad = minRad

    def area(self):
        self.area = self.majRad * self.minRad * math.pi
        return self.area

    def perimeter(self):
        return 'too hard to calculate'

    def __str__(self):
        return f'an ellipse with major radius {self.majRad}, and minor radius {self.minRad}'


class circle(ellipse):

    def __init__(self, radius):
        super(circle, self).__init__(radius, radius)
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius**2)
        self.area = area
        return self.area

    def perimeter(self):
        circumference = 2 * math.pi * self.radius
        self.perimeter = circumference
        return self.perimeter


    def __str__(self):
        return f'a circle with radius {self.radius}'



#class oval:




class polygon(shape):

    def __init__(self, numSides, length, height):
        super(polygon, self).__init__(self)
        self.numSides = numSides
        self.length = length
        self.height = height
        self.apothem = self.length / (2*math.tan(math.pi/self.numSides))

    def area(self):
        area = self.length * self.height
        self.area = area
        return area

    def perimeter(self):
        perimeter = self.length * self.numSides
        self.perimeter = perimeter
        return perimeter

class parallelogram(polygon):

    def __init__(self, length, height):
        super(parallelogram, self).__init__(4, length, height)

    def perimeter(self):
        perimeter = (2*self.length) + (2*self.height)
        self.perimeter = perimeter
        return perimeter

    def __str__(self):
        return f'a parallologram with base {self.length} and height {self.height}'



class rectangle(parallelogram):

    def __init__(self, length, height):
        super(rectangle, self).__init__(length, height)

    def __str__(self):
        statement = f'a ractangle with length {self.length} and height {self.height}'
        return statement


class rhombus(parallelogram):
    def __init__(self, diag1, diag2):
        super(rhombus, self).__init__(diag1, diag2)

    def perimeter(self):
        self.perimeter = 2 * (((self.length**2) + (self.height**2))**(1/2))
        return self.perimeter

    def area(self):
        self.area = self.length * self.height * (1/2)
        return self.area


    def __str__(self):
        return f'a rhombus with diagonals; {self.length} and {self.height}'

class square(rectangle):

    def __init__(self, side):
        super(square, self).__init__(side, side)

    def area(self):
        area = self.length**2
        self.area = area
        return area

    def __str__(self):
        statement = f'a square with length {self.length}'
        return statement

class triangle(polygon):

    def __init__(self, length, leg1, leg2, height):
        super(triangle, self).__init__(3, length, height)
        self.leg1 = leg1
        self.leg2 = leg2

    def area(self):
        area = int(self.height * self.length * 0.5)
        self.area = area
        return self.area

    def perimeter(self):
        perimeter = self.length + self.leg1 + self.leg2
        self.perimeter = perimeter
        return self.perimeter

    def __str__(self):
        return f'a triangle with sides; {self.length}, {self.leg1}, {self.leg2}'


class pentagon(polygon):                                            #assumes a regular pentagon

    def __init__(self, side):
        super(pentagon, self).__init__(5, side, side)

    def perimeter(self):
        perimeter = self.length * self.numSides
        self.perimeter = perimeter
        return self.perimeter


    def area(self):
        area = (5 * self.length * 0.5 * self.apothem)
        self.area = area
        return self.area


    def __str__(self):
        return f'a regular pentagon with side length {self.length}'









box = circle(5)


print(box.area())
print(box.perimeter())
print(box.numSides)
print(box)





