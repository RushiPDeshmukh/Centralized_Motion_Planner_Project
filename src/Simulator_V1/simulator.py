import pygame
import numpy as np
import pickle
import os
import random 
from Map_editor import *
from collections import defaultdict



"""
Loads the map file and visualises the map.
Starts a ROS node that reads the cars current node and updates the visual map to show the trajectory.
"""
#Parameters

win_width = 720
block_width = 20
path = os.path.abspath(os.path.dirname(__file__))
RED = (255,0,0)
DARK_RED = (200,0,0)
GREEN = (0,255,0)
DARK_GREEN = (0,200,0)
BLUE = (0,0,255)
DARK_BLUE = (0,0,200)
WHITE = (255,255,255)
BLACK = (0,0,0)
TURQUISE = (64,224,208)
ORANGE = (255,165,0)
GREY = (50,50,50)
YELLOW = (255,215,11)
DARK_YELLOW = (250,180,10)
SOFT_VIOLET = (225,175,253)
VIOLET = (147,0,255)

# win is the main display of the simulator
win = pygame.display.set_mode(size = (win_width*2,win_width))
pygame.display.set_caption("Simulator_V1")

#loading the map of the city from the map.pkl
# path = os.path.abspath(os.path.dirname(__file__))
# file = open(path+'\map.pkl','rb')
# rmap = pickle.load(file)




#dictionary variable to store the instances of cars
car_list = defaultdict()

class CAR:
    #This class will store the current cars in the env and its location. From the ros service we will update this location
    def __init__(self,pos,id,t) -> None:
        self.id = id
        self.pos = pos
        self.t = t
        # self.surface = pygame.image.load(path+ "//" +'car1.png')
        # self.surface = pygame.transform.scale(self.surface,(block_width,block_width))
        sample = np.random.randint(len(colors))
        self.color = colors[sample]
    def update_pos(self,pos,t):
        self.pos = pos
        self.t
        return True
    
    def draw(self,win):

        # car_rect = self.surface.get_rect()
        # car_rect.topleft = self.pos
        c = self.pos[0] + block_width//2 , self.pos[1] + block_width//2
        # win.blit(self.surface,car_rect)
        pygame.draw.circle(win,VIOLET,c,block_width//2)
        pygame.draw.circle(win,SOFT_VIOLET,c,block_width/2.5,2)
        

def render(win,rmap,cars_data,car_list): 
    cars_data = [tuple(cars_data[i]) for i in range(len(cars_data))]
    for car_data in cars_data:
        x,y,car_id,t = car_data
        pos = (x*block_width,y*block_width)
        if car_id in car_list.keys():
            car_list[car_id].update_pos(pos,t)
        else:
            car_list[car_id] = CAR(pos,car_id,t)
    draw_map(win,rmap)
    for _,c in car_list.items():
        c.draw(win)
    pygame.display.update()
    






# if __name__ == '__main__':
#     render(win,rmap,(0,(0,0),1),car_list)
#     pygame.time.delay(20000)