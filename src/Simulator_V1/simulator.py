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
SOFT_PINK = (247,139,209)
PINK = (156,34,93)
SOFT_BLU = (82,219,255)
BLU = (45,100,245)
color_cars1 = [VIOLET,PINK,BLU]
color_cars2 = [SOFT_VIOLET,SOFT_PINK,SOFT_BLU]
# win is the main display of the simulator
win = pygame.display.set_mode(size = (win_width*2,win_width))
pygame.display.set_caption("Simulator_V1")
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf',10)
text = font.render("T",True,BLACK)
textrect1 = text.get_rect()
textrect1.topleft = (1300,10)
textrect2 = text.get_rect()
textrect2.topleft = (1300,25)
textrect3 = text.get_rect()
textrect3.topleft = (1300,40)
textrect4 = text.get_rect()
textrect4.topleft = (1300,55)
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
        # sample = np.random.randint(len(colors))
        # self.color = colors[sample]
        sampler = self.id % 3
        self.color1 = color_cars1[sampler]
        self.color2 = color_cars2[sampler]
    
    def update_pos(self,pos,t):
        self.pos = pos
        self.t
        return True
    
    def draw(self,win):

        # car_rect = self.surface.get_rect()
        # car_rect.topleft = self.pos
        c = self.pos[0] + block_width//2 , self.pos[1] + block_width//2
        # win.blit(self.surface,car_rect)
        pygame.draw.circle(win,self.color1,c,block_width//2)
        pygame.draw.circle(win,self.color2,c,block_width/2.5,2)
        
def collision_check(cars_data):
    collision = False
    ids = []
    for car_datax in cars_data:
        xi,yi,car_idx,_ = car_datax
        for car_datay in cars_data:
            xj,yj,car_idy,_ = car_datay
            if xi == xj and yi == yj and car_idx != car_idy:
                collision = True
                if not car_idx in ids:
                    ids.append(car_idx)
                if not car_idy in ids:
                    ids.append(car_idy)
    
    return collision,ids


def render(win,rmap,cars_data,car_list,reached = 0, collision_count = 0,total_request = 0): 
    cars_data = [tuple(cars_data[i]) for i in range(len(cars_data))]
    time = 0
    for car_data in cars_data:
        x,y,car_id,t = car_data
        time = t
        pos1 = x,y
        pos = (x*block_width,y*block_width)
        if car_id in car_list.keys():
            car_list[car_id].update_pos(pos,t)
             
        else:
            car_list[car_id] = CAR(pos,car_id,t)
        if pos1 == (-1,-1):
                # print('Reached')
                reached +=1
                car_list.pop(car_id)   
    collision,colliding_cars_id = collision_check(cars_data)
    if collision:
        for id in colliding_cars_id:
            if id in car_list.keys():
                car_list.pop(id)
                collision_count +=1
        
    draw_map(win,rmap)
    for _,c in car_list.items():
        c.draw(win)
    text1 = font.render("Time: "+str(time),True,BLACK)
    win.blit(text1,textrect1)
    text2 = font.render("Total Request: "+str(total_request),True,BLACK)
    win.blit(text2,textrect2)
    text3 = font.render("Safe Reached Home: "+str(reached),True,BLACK)
    win.blit(text3,textrect3)
    text4 = font.render("Collisions Detected: "+str(collision_count),True,BLACK)
    win.blit(text4,textrect4)

   
    pygame.display.update()
    return reached,collision_count,colliding_cars_id
    






# if __name__ == '__main__':
#     render(win,rmap,(0,(0,0),1),car_list)
#     pygame.time.delay(20000)