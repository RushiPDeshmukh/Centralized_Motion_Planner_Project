import a_star 
import  car_gen
import time 
import numpy as np
from Trajectory_Checker import is_valid, correct_paths

def make_plan(start,goal,car_id = -1, t = 0, speed = 1, paths = None):
    #Wraps the car trajectory [x,y] into a tuple of [x,y,car_id,t]
    # paths = paths.reshape((-1,4))
    oldpath = a_star.main(start,goal)
    path = np.tile(oldpath,[1,2])
    for i in range(len(path)):
        path[i,3] = t + i * speed 
        path[i,2] = car_id
    # print('paths',paths)
    # valid,col_points = is_valid(path,paths)
    # print("validity:",valid)
    # print("collision points:",col_points)
    
    # print('t+1 option')
    valid,col_points =is_valid(path,paths)
    if not valid:
        path,valid,col_points = correct_paths(path,paths)
    
    # while not valid:

    #     print('A* modified')
    #     path = a_star.main(start,goal,col_points)
    #     path = np.tile(path,[1,2])
    #     for i in range(len(path)):
    #         path[i,3] = t + i * speed 
    #         path[i,2] = car_id
    #     valid,col_points = is_valid(path,paths)
    # print("Valid path found:",valid,i)
    
    return path


if __name__ == '__main__':
    pass


