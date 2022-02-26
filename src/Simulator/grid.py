import pygame
import numpy as np
from grid_tile import *

class grid():
    def __init__(self,grid_array,t = -1) -> None:
        """
        Args:
            grid_array ([np.array]): This will be a binary numpy array storing the city grid. 1 will represent road and 0 wil store buildings.
            t (int, optional): This will give the time element. Defaults to -1. This will be used to store the t slice for the grid object. 
        
        This class will be used to get a grid object at particular time t. This class's objects will store grid the of the city with cars in it. 
        """
        self.t = t
        self.shape = grid_array.shape
        self.data = grid_array
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



    def visualize(self):
        pass

    


