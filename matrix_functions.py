import math
import numpy as np


def translate(pos):
    tx, ty, tz = pos
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]
    ])


def rotate_x(m):
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(m), math.sin(m), 0],
        [0, -math.sin(m), math.cos(m), 0],
        [0, 0, 0, 1]
    ])


def rotate_y(m):
    return np.array([
        [math.cos(m), 0, -math.sin(m), 0],
        [0, 1, 0, 0],
        [math.sin(m), 0, math.cos(m), 0],
        [0, 0, 0, 1]
    ])


def rotate_z(m):
    return np.array([
        [math.cos(m), math.sin(m), 0, 0],
        [-math.sin(m), math.cos(m), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def scale(r):
    return np.array([
        [r, 0, 0, 0],
        [0, r, 0, 0],
        [0, 0, r, 0],
        [0, 0, 0, 1]
    ])
