import pygame as pg
import numpy as np
import math

class Camera:
    def __init__(self, render, position):
        self.render = render

        # camera position in world. position passed from main.py during init
        self.position = np.array([*position], 1)
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])

        # camera fov. angle in radians.
        self.h_fov = math.pi/2
        self.v_fov = self.h_fov * (render.height / render.width)

        # clipping planes
        self.near_plane = 0.1
        self.far_plane = 100

    def get_translate_matrix(self):
        """ returns translate matrix for camera matrix calculation """
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def get_rotate_matrix(self):
        """ returns rotational matrix for camera matrix calculation """
        rx, ry, rz, rw = self.right
        fx, fy, fz, fw = self.forward
        ux, uy, uz, uw = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    def camera_matrix(self):
        return self.get_translate_matrix() @ self.get_rotate_matrix()