"""
Bridge!

Problem
	* Two unrelated, parallel, or orthogonal abstractions
	* One: implementation-specific
    * Other: implementation-independent
"""


class DrawingAPIOne(object):
    """docstring for DrawingAPIOne"""

    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {})".format(x, y, radius))


class DrawingAPITwo(object):
    """docstring for DrawingAPIOne"""

    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {})".format(x, y, radius))


class Circle(object):

    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def scale(self, percent):
        self.radius *= percent

circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()

circle1 = Circle(4, 5, 6, DrawingAPITwo())
circle1.draw()
