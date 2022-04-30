import a_star 
import  car_gen
import time 
import numpy as np
from Trajectory_Checker import is_valid

def make_plan(start,goal,car_id = -1, t = 0, speed = 1,collisions = None, paths = None):
    #Wraps the car trajectory [x,y] into a tuple of [x,y,car_id,t]
    # paths = paths.reshape((-1,4))
    oldpath = a_star.main(start,goal,collisions)
    path = np.tile(oldpath,[1,2])
    for i in range(len(path)):
        path[i,3] = t + i * speed 
        path[i,2] = car_id
    # print('paths',paths)
    v,c_p = is_valid(path,paths)
    print("validity:",v)
    print("collision points:",c_p)
    
    if not v:
        print('A* modified')
        path = a_star.main(start,goal,c_p)
        path = np.tile(path,[1,2])
        for i in range(len(path)):
            path[i,3] = t + i * speed 
            path[i,2] = car_id
        v,c_p = is_valid(path,paths)
        print("validity after changing:",v,i)
    
   
    return path


if __name__ == '__main__':
    pass


