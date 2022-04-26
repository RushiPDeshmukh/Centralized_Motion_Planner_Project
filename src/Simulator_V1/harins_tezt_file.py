import numpy as np
import car_gen
import a_star
from simulator import *
# import pygame

map_path = '//map.pkl'
dir_path = os.path.abspath(os.path.dirname(__file__))
path = dir_path + map_path
file = open(path,'rb')
rmap =  pickle.load(file)

paths = []
s1,g1 = car_gen.main()
path1 = a_star.main(s1,g1)
paths.append(path1)

s2,g2 = car_gen.main()
path2 = a_star.main(s2,g2)
paths.append(path2)

# print(path)
for i in range(len(paths)):
    tuple = (0,(block_width*path[i,0],block_width*path[i,1]),1)
    # print(tuple)
    render(win,rmap,tuple,car_list)
    pygame.time.delay(200)