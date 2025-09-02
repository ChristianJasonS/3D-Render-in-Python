from math import *
import numpy as np

class Projection:
    def __init__(self, render):
        # retrieve near and far plane from camera
        self.near = render.camera.near_plane
        self.far = render.camera.far_plane

        # calculate right, left, top, bottom length in the projection plane
        self.right = tan(self.render.camera.h_fov/2)
        self.left = -self.right
        self.top = tan(self.render.camera.v_fov/2)
        self.bottom = -self.top

        # set up projection matrix. projection matrix moves the matrix from
        # camera space to clip space
        m00 = 2 / (self.right - self.left)
        m11 = 2 / (self.top - self.bottom)
        m22 = (self.far + self.near) / (self.far - self.near)
        m32 = -2 * self.near * self.far / (self.far - self.near)
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])