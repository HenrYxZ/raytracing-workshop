from camera import Camera
from scene import Scene, Sphere
from render import render


def main():
    # Create a Camera
    camera = Camera()

    # Create a Scene
    scene = Scene()
    sphere = Sphere()
    scene.add(sphere)

    # Render the scene from the camera
    image = render(scene, camera)

    # Save the image into a file
    image.save("output.png")


if __name__ == '__main__':
    main()
