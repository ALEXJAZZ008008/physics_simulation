import math


class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))
