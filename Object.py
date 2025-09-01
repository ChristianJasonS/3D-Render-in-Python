import pygame as pg
import numpy as np
from matrix_functions import *

class Object:
    def __init__(self, render):
        self.render = render
        self.vertices = None

    def render(self):
        pass

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
