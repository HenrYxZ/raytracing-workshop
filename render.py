from camera import Camera
import numpy as np
from PIL import Image
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
            pass
        pass
    image = Image.fromarray(arr)
    return image
