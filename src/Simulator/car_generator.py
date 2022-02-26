import numpy as np 
from car import *

def car_generator(node_list):
    nodes = np.load('node_list.npy')
    start_index = np.random.randint(0,len(nodes))
    start_position = [nodes[start_index,0],nodes[start_index,1]]
    goal_index = np.random.randint(0,len(nodes))
    goal_position = [nodes[goal_index,0],nodes[goal_index,1]]
    