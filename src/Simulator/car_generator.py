import numpy as np 
from car import *

# used to randomly generate new cars
def car_generator(node_list,interval,number_cars):
    """node_list is a list of points where the cars can spawn or have destinations"""
    nodes = np.load('node_list.npy')
    ID = 0
    car_list = []
    for i in range(number_cars):
        ID = ID + 1
        start_index = np.random.randint(0,len(nodes))
        start_position = [nodes[start_index,0],nodes[start_index,1]]
        goal_index = np.random.randint(0,len(nodes))
        goal_position = [nodes[goal_index,0],nodes[goal_index,1]]
        car_list = car_list.append[car(t,start_position,goal_position,ID)]
        t = t + interval
