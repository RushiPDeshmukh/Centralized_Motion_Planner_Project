import pygame
import numpy as np
import pickle
import os
import random 



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


if __name__ == "__main__":

    win = pygame.display.set_mode(size = (win_width*2,win_width))
    pygame.display.set_caption("Simulator_V1")
    
    path = os.path.abspath(os.path.dirname(__file__))
    file = open(path+'/map.pkl','rb')
    rmap = pickle.load(file)

    row = 0
    col = 0
    episode = True
    road_toggle = False
    while episode:
        
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                episode = False
            if pygame.mouse.get_pressed()[0]: #LEFT_Click
                pos = pygame.mouse.get_pos()
                row, col = (pos[0]//block_width,pos[1]//block_width)
            if pygame.mouse.get_pressed()[1]:#RIGHT_Click
                pos = pygame.mouse.get_pos()
                rmap[pos[0]//block_width][pos[1]//block_width].change_type("house")
            #Change Type of the block  
            if ev.type == pygame.KEYDOWN:  
                if ev.key == pygame.K_r:
                    road_toggle = not road_toggle
                if ev.key == pygame.K_i:
                    rmap[row,col].change_type("road")
                    
                if ev.key == pygame.K_h:
                    rmap[row,col].change_type("house")
                     
                if ev.key == pygame.K_c:
                    rmap[row,col].change_type("complex")
                if ev.key == pygame.K_d:
                    rmap[row,col].change_type("off_road")
                

                #Move accros the map    
                if ev.key == pygame.K_UP:
                    if col-1 >= 0:
                        col -= 1
                    if road_toggle: rmap[row,col].change_type("road")
                if ev.key == pygame.K_DOWN:
                    if col+1 < win_width/block_width:
                        col +=1
                    if road_toggle: rmap[row,col].change_type("road")
                if ev.key == pygame.K_LEFT:
                    if row-1 >= 0:
                        row -= 1
                    if road_toggle: rmap[row,col].change_type("road")
                if ev.key == pygame.K_RIGHT:
                    if row+1 < win_width*2/block_width:
                        row += 1
                    if road_toggle: rmap[row,col].change_type("road")

                #Save the rmap 
                if ev.key ==pygame.K_s:
                    store(rmap,path)
            rmap[row,col].draw_pointer(win)            
            draw_map(win,rmap)