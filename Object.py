import pygame as pg
import numpy as np
from matrix_functions import *

class Object:
    def __init__(self, render):
        self.render = render
        self.vertices = None

    def screen_project(self):
        """calculates the vertices matrix to project object to:
        1. camera space, then
        2. projection space or clip space, then
        3a. normalize vertices by dividing each row by its last column
        3b. replace vertices outside (-1, 1) with 0 to avoid rendering vertices
            beyond 'view'
        3c. project normalized vertices to screen based on screen resolution
        """
        # move object vertices to camera space.
        vertices = self.vertices @ self.render.camera.camera_matrix()

        # move object vertices from camera space to clip space.
        vertices = vertices @ self.render.projection.projection_matrix

        # normalize by dividing each row with its last column
        # retrieves the last column of each row
        w_column = vertices[:, -1]
        # reshapes array into rows of one column
        w_column.reshape(-1, 1)
        # divide each row with its last column
        vertices = vertices / w_column

        # remove vertices outside (-1, 1)
        # matrix_a & matrix_b contain a matrix of True False values.
        matrix_a = vertices > 1
        matrix_b = vertices < -1
        # if any element is True (outside range), element is replaced with 0
        # 'matrix_a | matrix_b' functions as a mask
        vertices[matrix_a | matrix_b] = 0

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, ratio):
        self.vertices = self.vertices @ scale(ratio)

    def rotate_x(self, rad):
        self.vertices = self.vertices @ rotate_x(rad)

    def rotate_y(self, rad):
        self.vertices = self.vertices @ rotate_y(rad)

    def rotate_z(self, rad):
        self.vertices = self.vertices @ rotate_z(rad)
