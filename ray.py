from pyglet.math import Vec3
from math import sqrt

from scene import Sphere


class Ray:
    def __init__(self, pr: Vec3, nr: Vec3):
        self.pr = pr
        self.nr = nr

    def intersect_sphere(self, obj: Sphere) -> float:
        diff = self.pr - obj.pos
        b = self.nr.dot(diff)
        c = diff.dot(diff) - obj.r ** 2
        discriminant = b ** 2 - c

        if discriminant < 0:
            return -1.0
        t = -b - sqrt(discriminant)
        return t

    def intersect(self, obj) -> float:
        if isinstance(obj, Sphere):
            return self.intersect_sphere(obj)

        raise NotImplementedError(
            f"object of type: {type(obj)} doesn't have intersect function"
        )


    def at(self, t: float) -> Vec3:
        return self.pr + self.nr * t
