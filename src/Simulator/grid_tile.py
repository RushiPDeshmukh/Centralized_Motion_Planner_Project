from turtle import pos
import pygame
import numpy as np
from sklearn import neighbors


GREY = (150,150,150)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

class Grid_tile():
    """
    This class will give you the behaviour of each tile on the grid.
    type : type of tile can be CAR, ROAD, OBSTACLE which will be indicated by the color of the tile

    Functions:

    get_neighbourse(): will take 

    """
    def __init__(self,pos,value,width):
        self.pos = pos
        self.x = pos[0]*width
        self.y = pos[1]*width
        self.value = value
        self.color = WHITE if value == 0 else GREY
        self.width = width
        self.dir_row = [-1, 1, 0, 0]
        self.dir_col = [0, 0, 1, -1]

    def draw(self,win):
        pygame.draw.rect(win,self.color,rect = (self.x,self.y,self.width,self.width))

    def get_neighbours(self, grid, pos, dir):
        """
        Given a node it will check of feasable neighbours of the node.
        grid : The grid in which the nodes are present
        pos : position of where the node is located in the grid
        dir : direction of where the node can explore
        """
        neighbors = []
        max_rows, max_cols = grid.shape
        r, c = pos
        for i in list(dir):
            if i == 'E':
                rr = r + 1
            if i == 'W':
                rr = r - 1
            if i == 'N':
                cc = c + 1
            if i == 'S':
                cc = c - 1
            if rr < 0 or cc < 0:
                continue
            if rr > max_rows or cc > max_cols:
                continue
            if grid[rr][cc] == 0:
                continue
            neighbors.append([rr, cc])    
        return neighbors

