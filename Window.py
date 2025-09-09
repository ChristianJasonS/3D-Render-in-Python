import pygame as pg
from Object import *
from Cube import *
from Camera import *
from Projection import *
from matrix_functions import *

run = True

class SoftwareRender:
    def __init__(self):
        self.resolution = (1470, 820)
        self.w_height = self.resolution[1]
        self.w_width = self.resolution[0]

        self.fps = 60
        self.screen = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()
        # Needed later for clipping since 0,0 is the center of the screen.
        self.half_w_height = self.w_height // 2
        self.half_w_width = self.w_width // 2

        self.background_colour = (10, 10, 10)

        self.camera = Camera(self, [1, 1, -4])
        self.projection = Projection(self)
        self.create_cube()
        # self.create_camera(np.array([0, 0, 0]))
        # self.create_projection()

    def draw(self):
        self.screen.fill(self.background_colour) # colour background first

        self.cube.screen_project()


    def create_cube(self):
        self.cube = Cube(self)
        self.cube.translate([0.2, 0.4, 0.2])
        self.cube.rotate_y(math.pi / 6)
        # draw cube in


    def create_camera(self, position):
        self.camera = Camera(self, position)


    def create_projection(self):
        self.projection = Projection(self)


    def run(self):
        # surface for drawing transparent polygons
        # self.a_screen = pg.Surface((self.w_height, self.w_width), pg.SRCALPHA)
        # pg.display.set_caption('Simple Python Render')
        # run = True

        # for each tick, check event, update screen
        while True:
            # calls draw method,
            self.draw()

            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.fps)
            # iterate through events list and process events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                    # break

            # update window display

            # pg.display.flip() # display all



