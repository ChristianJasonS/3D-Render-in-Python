import pygame as pg
import numpy as np
from matrix_functions import *

class Object:
    def __init__(self, render):
        self.render = render
        self.vertices = None
        self.faces = None

    def screen_project(self):
        """calculates the vertices matrix to project object to:
        1. camera space, then
        2. projection space or clip space, then
        3a. normalize vertices by dividing each row by its last column
        3b. replace vertices outside (-1, 1) with 0 to avoid rendering vertices
            beyond 'view'
        3c. project normalized vertices to screen based on screen resolution
        4. Display each face of the object
        """
        # move object vertices to camera space.
        vertices = self.vertices @ self.render.camera.camera_matrix()

        # move object vertices from camera space to clip space.
        vertices = vertices @ self.render.projection.projection_matrix

        # normalize by dividing each row with its last column
        # vertices /= vertices[:, -1].reshape(-1, 1)

        # TODO: uncomment
        # retrieves the last column of each row
        w_column = vertices[:, -1]
        # # reshapes array into rows of one column
        w_column = w_column.reshape(-1, 1)
        # # divide each row with its last column
        vertices = vertices / w_column

        # remove vertices outside (-1, 1)
        # vertices[(vertices > 1) | (vertices < -1)] = 0
        # matrix_a & matrix_b contain a matrix of True False values.
        matrix_a = vertices > 1
        matrix_b = vertices < -1
        # if any element is True (outside range), element is replaced with 0
        # 'matrix_a | matrix_b' functions as a mask
        vertices[matrix_a | matrix_b] = 0

        # project normalized vertices to screen resolution
        vertices = vertices @ self.render.projection.to_screen_matrix
        # slice matrix to retrieve x,y coordinates on screen
        vertices = vertices[:, :2]

        # Display faces
        for faces in self.faces:  # faces is a 4x1 numpy array containing the
            # index of each vertice coordinate
            polygon = vertices[faces]
            # draw each face (polygons)
            # prevent vertices lying on the screen edge from being drawn
            if not np.any((polygon == self.render.half_w_height) |
                          (polygon == self.render.half_w_width)):
                pg.draw.polygon(self.render.screen, pg.Color('orange'), polygon, 3)

            # draw each vertex (dots)
        for vertex in vertices:
            if not np.any((vertex == self.render.half_w_height) |
                          (vertex == self.render.half_w_width)):
                pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)

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
