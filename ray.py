from math import sqrt
from pyglet.math import Vec3


class Ray:
    def __init__(self, pr: Vec3, nr: Vec3):
        self.pr = pr
        self.nr = nr

    def intersect(self, sphere):
        diff = self.pr - sphere.pos
        b = self.nr.dot(diff)
        c = diff.dot(diff) - sphere.r ** 2
        discriminant = b ** 2 - c

        if discriminant < 0:
            return -1.0

        t = -b - sqrt(discriminant)
        return t
