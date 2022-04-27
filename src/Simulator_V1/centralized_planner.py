import a_star 
import  car_gen
import time 
import numpy as np

def make_plan(start,goal,car_id = -1, t = 0, speed = 1):

    path = a_star.main(start,goal)
    path = np.tile(path,[1,2])
    for i in range(len(path)):
        path[i,3] = t+ i * speed 
        path[i,2] = car_id

    return path


