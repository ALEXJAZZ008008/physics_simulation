import math
import vector2d


class Vector3D(vector2d.Vector2D):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dot(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
