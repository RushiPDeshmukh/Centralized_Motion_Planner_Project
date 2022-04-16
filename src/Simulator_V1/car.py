import pygame
import numpy as np
from grid import *

class CAR:
    def __init__(self,t,start_pos,goal_pos,ID):
        self.ID = ID
        self.start_position = start_pos
        self.goal_position = goal_pos
        self.position = self.get_position(t)
        self.speed = 1
        self.initial_time = t

# path for vehicle given by central planner
    def get_path(self,path):
        """ 
        'path' is the path provided to the car by the central planner
        get_path stores the path for the car
        """
        self.path = path        # path is a 2D array of x,y positions
        pass

# Get position at a current point in time
    def get_position(self,t):
        """
        t is current time for which we want the position of the car
        get_position() gives us the position of the car at instant 't'
        """
        delta_t = t - self.initial_time         # to calculate the position of the car with respect to the time it spwaned
        x_pos,y_pos = self.path[delta_t]
        return x_pos,y_pos

    def get_path(self):
        ''''''


def start_goal_pos():
    locations = np.load('dest_node')
    start_index = np.random.randint(locations.shape[0])
    end_index = np.random.randint(locations.shape[0])
    


car1 = CAR(t = 0, )

if __name__ == "__main__":
    pass