from pyglet.math import Vec3

from camera import Camera
from ray import Ray
from scene import Scene


def compute_color(
    i: int, j: int, width: int, height: int, scene: Scene,
    camera: Camera
) -> Vec3:
    color = Vec3()

    # Crear rayo
    pp = camera.project_point(i, j, width, height)
    nr = (pp - camera.position).normalize()
    ray = Ray(camera.position, nr)
    min_t = float('inf')
    min_obj = None

    for obj in scene.objects:
        t = ray.intersect(obj)
        if 0 < t < min_t:
            min_t = t
            min_obj = obj

    if min_obj:
        ph = ray.at(min_t)
        n = min_obj.normal_at(ph)
        l = Vec3(0.0, 1.0, 0.0).normalize()
        ilum = min(max(0.0, n.dot(l)), 1.0)
        ilum = max(0.2, ilum)
        color = Vec3(1.0, 1.0, 1.0)
        color *= ilum

    return color
