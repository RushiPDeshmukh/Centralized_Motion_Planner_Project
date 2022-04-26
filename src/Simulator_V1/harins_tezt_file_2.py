import numpy as np
import car_gen
import a_star
from simulator import *
import time
# import pygame

map_path = '//map.pkl'
dir_path = os.path.abspath(os.path.dirname(__file__))
path = dir_path + map_path
file = open(path,'rb')
rmap =  pickle.load(file)

paths = []
for i  in range(3):
    s,g = car_gen.main()
    paths.append(a_star.main(s,g))

t = 0
simtime = 0
tic = time.time()


print("Paths:",paths[:])

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