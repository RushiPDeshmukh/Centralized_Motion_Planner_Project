from tracemalloc import start
# import pygame
import numpy as np
import os
# from grid import *

class CAR:
    def __init__(self,t,start_pos,goal_pos,ID):
        self.ID = ID
        self.start_position = start_pos
        self.goal_position = goal_pos
        self.position = self.get_position(t)
        self.speed = 1
        self.initial_time = t

# path for vehicle given by central planner
    def store_path(self,path):
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
        '''
        send start and goal positions via ROS to a_star mapper
        get trajectory in return 
        '''
        self.start_position
        self.goal_position


def start_goal_pos_gen():
    '''
    chooses random start and goal location on the map
    'dest.node' is a numpy array of all points that can be start or goal positions
    '''
    map_path = '//dest_node.npy'
    dir_path = os.path.abspath(os.path.dirname(__file__))
    path = dir_path + map_path
    locations =  np.load(path)

    start_index,goal_index = 0,0
    while start_index == goal_index:
        start_index = np.random.randint(locations.shape[0])
        goal_index = np.random.randint(locations.shape[0])
    start_pos = locations[start_index].astype(np.int32).tolist()
    goal_pos = locations[goal_index].astype(np.int32).tolist()
    return start_pos, goal_pos


def main():
    s,g = start_goal_pos_gen()
    print(s,g)
    return s,g
    # car1 = CAR(t = 0, start_pos = s, goal_pos = g, ID = 1)
    # car1.get_path()

if __name__ == "__main__":
    main()