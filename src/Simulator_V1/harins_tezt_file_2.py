import numpy as np
import car_gen
import a_star
from simulator import *
import time
from centralized_planner import *
# import pygame

map_path = '//map.pkl'
dir_path = os.path.abspath(os.path.dirname(__file__))
path = dir_path + map_path
file = open(path,'rb')
rmap =  pickle.load(file)

num_cars = 10
paths = np.empty((1,4))
for i  in range(num_cars):
    s,g = car_gen.main()
    car_id = i
    paths = np.append(paths,make_plan(s,g,car_id))


paths = paths.reshape((-1,4))
paths = paths[paths[:,3].argsort()].astype(np.int16)

# print("Paths:",paths)

for i in range(max(paths[:,3])):
    tuple_list = paths[paths[:,3]==i]
    render(win,rmap,tuple_list,car_list)
    pygame.time.delay(100)

# while simtime < 20:
#     toc = time.time()
#     simtime = toc-tic
#     t = t+1
#     for i in range(len(paths)):
#         try:
#             path = paths[i]
#             tuple = (0,(block_width*path[t,0],block_width*path[t,1]),1)
#     #         # print(tuple)
            
#             render(win,rmap,tuple_list,car_list)
#         except:
#             pass
#             pygame.time.delay(10)
#     pygame.time.delay(30)