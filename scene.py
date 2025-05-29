from pyglet.math import Vec3


class Scene:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)


class Sphere:
    def __init__(self, pos: Vec3 = Vec3(), r: float = 1.0):
        self.pos = pos
        self.r = r

    def normal_at(self, p: Vec3) -> Vec3:
        n = (p - self.pos).normalize()
        return n
