from pyglet.math import Vec3

from camera import Camera
from ray import Ray
from scene import Scene



def compute_color(
    i: int, j: int, width: int, height: int, scene: Scene, camera: Camera
) -> Vec3:
    color = Vec3()
    pp = camera.project_point(i, j, width, height)
    nr = (pp - camera.position).normalize()
    ray = Ray(camera.position, nr)
    min_obj = None
    min_t = float('inf')

    for obj in scene.objects:
        t = ray.intersect(obj)
        if t < min_t:
            min_t = t
            min_obj = obj

    if min_t > 0:
        ph = ray.pr + ray.nr * min_t
        l = Vec3(0.0, 1.0, 0.0)
        n = obj.normal_at(ph)
        ilum = n.dot(l)
        ilum = max(0.2, ilum)
        color = Vec3(0.0, 0.0, 0.8)
        color = color * ilum

    return color
