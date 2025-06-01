from camera import Camera
import numpy as np
from PIL import Image

import raytracer
from scene import Scene


WIDTH = 288
HEIGHT = 192
COLOR_CHANNELS = 3
MAX_COLOR_VALUE = 255


def render(scene: Scene, camera: Camera) -> Image:
    arr = np.zeros([HEIGHT, WIDTH, COLOR_CHANNELS], dtype=np.uint8)
    # Compute the color for each pixel
    for j in range(HEIGHT):
        for i in range(WIDTH):
            color = raytracer.compute_color(i, j, WIDTH, HEIGHT, scene, camera)
            rgb_color = color * 255
            arr[j, i] = rgb_color
    image = Image.fromarray(arr)
    return image
