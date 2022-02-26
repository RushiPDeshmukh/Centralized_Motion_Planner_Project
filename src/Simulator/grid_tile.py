import pygame
import numpy as np


GREY = (150,150,150)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

class Grid_tile():
    """
    This class will give you the behaviour of each tile on the grid.
    type : type of tile can be CAR, ROAD, OBSTACLE


    """
    def __init__(self,pos,value,width):
        self.pos = pos
        self.x = pos[0]*width
        self.y = pos[1]*width
        self.value = value
        self.color = GREY if value == 1 else WHITE
        self.width = width
        

    def draw(self,win):
        pygame.draw.rect(win,self.color,rect = (self.x,self.y,self.width,self.width))

    def get_neighbours(self):
        pass

