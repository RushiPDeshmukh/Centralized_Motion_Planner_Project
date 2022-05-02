import numpy as np
import car_gen
from simulator import *
import time
from centralized_planner import *
# import pygame

map_path = '//map.pkl'
dir_path = os.path.abspath(os.path.dirname(__file__))
path = dir_path + map_path
file = open(path,'rb')
rmap =  pickle.load(file)

reached = 0
collision_count = 0
total_requests = 0

if __name__ == "__main__":
    t =  0
    while t < 3000:
        num_cars = np.random.randint(3,10)
        total_requests += num_cars
        print("|| num_cars:",num_cars,'|| time: ',t,"||")

        paths = np.empty((1,4))
        for i  in range(num_cars):
            s,g = car_gen.main()
            car_id = i
            path = make_plan(s,g,car_id,paths = paths,t=t)
            paths = np.append(paths,path)

            paths = paths.reshape((-1,4))

        paths = paths[1:,:]
        paths = paths[paths[:,3].argsort()].astype(np.int16)

        # print("Paths:",paths)
        
        for i in range(min(paths[:,3]),max(paths[:,3])+1):
            tuple_list = paths[paths[:,3]==i]
            t = i
            reached,collision_count,colliding_ids = render(win,rmap,tuple_list,car_list,reached,collision_count,total_requests)
            for id in colliding_ids:
                index = paths[:,2]==id
                paths = np.delete(paths,index,0)
            pygame.time.delay(20)
        
    print("reached:",reached,' | total request:',total_requests,' | collision count:',collision_count)

        

   