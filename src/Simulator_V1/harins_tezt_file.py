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

s,g = car_gen.main()
path = a_star.main(s,g)
print(path)
for i in range(path.shape[0]):
    tuple = (0,(block_width*path[i,0],block_width*path[i,1]),1)
    # print(tuple)
    render(win,rmap,tuple,car_list)
    pygame.time.delay(200)