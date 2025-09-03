import pygame as pg
from Object import *
from Cube import *
from Camera import *

run = True

class Window:
    def __init__(self, resolution):
        self.w_height = resolution[0]
        self.w_width = resolution[1]
        self.background_colour = (200, 200, 200)
        self.create_object()

    def create_object(self):
        self.cube = Cube(self)
        # draw cube in

    def create_camera(self, position):
        self.camera = Camera(self, position)

    def display(self):
        screen = pg.display.set_mode((self.w_height, self.w_width))
        pg.display.set_caption('Simple Python Render')
        run = True

        # for each tick, check event, update screen
        while(run):

            # iterate through events list and process events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    # break

            # update window display
            screen.fill(self.background_colour) # colour background first

            pg.display.flip() # display all



