import pygame
import numpy as np
from grid_tile import *
import os

path = os.path.abspath(os.path.dirname(__file__))
class grid():
    def __init__(self,grid_array,grid_dir,t = -1) -> None:
        """
        Args:
            grid_array ([np.array]): This will be a binary numpy array storing the city grid. 1 will represent road and 0 will store buildings.
            grid_dir ([np.array]): This will be a string numpy array storing the direction of gridtiles.
            t (int, optional): This will give the time element. Defaults to -1. This will be used to store the t slice for the grid object. 
        
        This class will be used to get a grid object at particular time t. This class's objects will store grid the of the city with cars in it. 
        """
        self.t = t
        self.shape = grid_array.shape
        self.data = make_grid(grid_array,grid_dir)
        self.x = self.shape[0]
        self.y = self.shape[1]
        return None

    def make_graph(self):
        """
        This function will be used generate a weighted graph at time t.
        """
        for i in range(self.x):
            for j in range(self.y):
                pass
    
    def make_grid(self,grid_array,grid_dir):
        """
        Args:
            grid_array ([np.array]): This will be a binary numpy array storing the city grid. 1 will represent road and 0 will store buildings.
            grid_dir ([np.array]): This will be a string numpy array storing the direction of gridtiles.

        This function will make a grid of data type gridtile based on numpy array of grid_array and grid_dir.
        """
        pass
    


    def visualize(self):
        pass

#map_grid will contain a numpy array with binary values. 1s representing roads and 0s representing buildings.
map_grid = np.load(path + "map_grid.npy")
#map_dir will contain a direction
map_dir = np.load(path + "map_dir.npy")





    


