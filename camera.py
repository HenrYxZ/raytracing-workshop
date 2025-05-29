from pyglet.math import Vec3


class Camera:
    def __init__(
        self,
        position: Vec3 = Vec3(0.0, 0.0, -4.0),
        v_view: Vec3 = Vec3(0.0, 0.0, 1.0),
        v_up: Vec3 = Vec3(0.0, 1.0, 0.0),
        d: float = 26,
        sx: float = 35,
        sy: float = 24
    ):
        self.position = position
        self.v_view = v_view
        self.v_up = v_up
        self.d = d
        self.sx = sx
        self.sy = sy

        # Calculate basis
        self.n0 = self.v_up.cross(v_view).normalize()
        self.n2 = self.v_view.normalize()
        self.n1 = self.n2.cross(self.n0).normalize()

        # Calculate p00
        pc = self.position + self.v_view * d
        self.p00 = pc - self.n0 * sx / 2.0 - self.n1 * sy / 2.0

    def project_point(self, i: float, j: float, width: int, height: int) -> (
        Vec3
    ):
        xp = (i / width) * self.sx
        yp = ((height - j) / height) * self.sy
        pp = self.p00 + self.n0 * xp + self.n1 * yp
        return pp
