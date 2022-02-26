import numpy as np 
from car import *

# used to randomly generate new cars
def car_generator(node_list,interval):
    """node_list is a list of points where the cars can spawn or have destinations"""
    nodes = np.load('node_list.npy')
    start_index = np.random.randint(0,len(nodes))
    start_position = [nodes[start_index,0],nodes[start_index,1]]
    goal_index = np.random.randint(0,len(nodes))
    goal_position = [nodes[goal_index,0],nodes[goal_index,1]]
    
    t = 0
    c1 = car(t,start_position,goal_position)
    t = t + interval
    c2 = car(t,start_position,goal_position)