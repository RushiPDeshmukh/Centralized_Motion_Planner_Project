import pygame
import numpy as np
import pickle
import os
import random 

################ This version is to make the map look like a mini motorways sim ##################

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

#BG_COLOR = (236,110,110)
BG_COLOR = (60,200,180)

colors = [RED,BLUE,GREEN]
dark_colors = [DARK_RED,DARK_BLUE,DARK_GREEN]

win_width = 720
block_width = 20

class BLOCKS:
    def __init__(self, row, col, block_width):
        self.rtype = 'off_road'
        self.dir = 'SE'
        self.row = row
        self.col = col
        self.x = row * block_width
        self.y = col * block_width
        self.center = (self.x+(block_width/2), self.y+(block_width))
        self.width = block_width
        self.top_left = -1
        self.top_right = -1
        self.bottom_left = -1
        self.bottom_right = -1
        self.neighbours = []
        self.color1 = RED
        self.color2 = DARK_RED
        

    def change_type(self, t):
        self.rtype = t

    def draw(self,win):
        if self.rtype == "road":
            pygame.draw.rect(win,GREY,rect=(self.x,self.y,self.width,self.width),border_top_left_radius=self.top_left,border_top_right_radius=self.top_right,border_bottom_left_radius=self.bottom_left,border_bottom_right_radius=self.bottom_right)
        elif self.rtype == "house":
            pygame.draw.rect(win,self.color1,rect=(self.x,self.y,self.width,self.width/2))
            pygame.draw.rect(win,self.color2,rect=(self.x,self.y+(self.width/2),self.width,self.width/2))
        elif self.rtype == "complex":
            pygame.draw.rect(win,YELLOW,rect=(self.x,self.y,self.width*2,self.width*2),border_radius=8)
            pygame.draw.circle(win,DARK_YELLOW,(self.x+self.width,self.y+self.width),self.width,5)
        

    def draw_pointer(self,win):
        pygame.draw.rect(win,TURQUISE,pygame.Rect(self.x,self.y,self.width,self.width),2)
        pygame.display.update()
    

def init_map(block_width, win_width,node = BLOCKS):
    row_map = (win_width*2)//block_width
    col_map = win_width//block_width
    Empty_map = np.empty((row_map,col_map),dtype= node)
    print(Empty_map.shape)
    for i in range(row_map):
        for j in range(col_map):
            Empty_map[i][j] = node(row= i,col = j,block_width=block_width)
    return Empty_map

def draw_map(win, map):
    win.fill(BG_COLOR)
    row_map, col_map = map.shape
    for i in range(row_map):
        for j in range(col_map):
            map[i][j].draw(win)
    pygame.display.update()

def store(rmap,path,np_grid=False):
    if np_grid:
        grid = np.zeros(rmap.shape)
        row_map, col_map = rmap.shape
        for i in range(row_map):
            for j in range(col_map):
                grid[i][j] = 1 if rmap[i][j].rtype == "off_road" else 0
        np.save(path+'//grid_map.npy',grid)
        print("Grid_Map Saved!")
    else:
        file = open(path+'//map.pkl','wb')
        pickle.dump(rmap,file)

def store_nodes(rmap):
    list_nodes = []
    row_map, col_map = rmap.shape
    for i in range(row_map):
        for j in range(col_map):
            if rmap[i][j].rtype == "house" or rmap[i][j].rtype == "complex" :
                list_nodes.append((i,j))
    list_nodes = np.array(list_nodes)
    np.save(path+'//dest_node.npy',list_nodes)
    print("List of  Saved!")

def main(rmap = None,save_np = False):
    """loads the rmap pickle file and visualizes the map in pygame env.
        It also lets the user edit the map and save changes to the map.
    """
    win = pygame.display.set_mode(size = (win_width*2,win_width))
    pygame.display.set_caption("Simulator_V1")
    
    path = os.path.abspath(os.path.dirname(__file__))
    if rmap == None:
        file = open(path+'/map.pkl','rb')
        rmap = pickle.load(file)
    else:
        rmap = init_map(block_width,win_width)
    if save_np:
        store(rmap,path,True)
        store_nodes(rmap)

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

if __name__  =="__main__":
    main(None,True) 
        




        
