import pygame
import numpy as np
import pickle



RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
TURQUISE = (64,224,208)
ORANGE = (255,165,0)
GREY = (150,150,150)

win_width = 750
block_width = 15
win = pygame.display.set_mode(size = (win_width,win_width))
pygame.display.set_caption("Title")

class Blocks:
    def __init__(self, row, col, block_width):
        self.rtype = 'straight'
        self.angle = 0
        self.road = np.array([[0,1,0],[0,1,0],[0,1,0]])
        self.row = row
        self.col = col
        self.x = row * block_width
        self.y = col * block_width
        self.width = block_width
        self.spacing = block_width//3

    def change_type(self, t):
        self.rtype = t
        if self.rtype == 'straight':
            self.road = np.array([[0,0,0],[1,1,1],[0,0,0]])
        if self.rtype == 'turn':
            self.road = np.array([[0,0,0],[0,1,1],[0,1,0]])
        if self.rtype == 'T':
            self.road = np.array([[0,0,0],[1,1,1],[0,1,0]])
        if self.rtype == 'plus':
            self.road = np.array([[0,1,0],[1,1,1],[0,1,0]])
        if self.rtype == 'void':
            self.road = np.array([[0,0,0],[0,0,0],[0,0,0]])

    def add_state(self,list):
        status = str(self.row)+" "+str(self.col)+" "+self.rtype+" "+str(self.angle)
        list.append(status)
    
    def rotate(self):
        self.road = np.rot90(self.road)

    def draw(self,win):
        for i in range(3):
            for j in range(3):
                if self.road[i,j]==1:
                    color = GREY
                elif self.road[i,j]==0:
                    color = WHITE
                pygame.draw.rect(win,color=color,rect=(self.x + i*self.spacing,self.y + j*self.spacing,self.width,self.width))
    def draw_pointer(self,win):
        pygame.draw.rect(win,TURQUISE,pygame.Rect(self.x,self.y,self.width,self.width),2)
        pygame.display.update()

    def add_to_grid(self,grid):
        for i in range(3):
            for j in range(3):
                grid[self.row*3 + i,self.col*3 + j] = self.road[i][j]
        
        return grid

def init_map(block_width = 15, win_width = 900):
    row_map = win_width//block_width
    col_map = win_width//block_width
    Empty_map = np.empty((row_map,col_map),dtype= Blocks)
    no_blocks = int(win_width/block_width)
    for i in range(no_blocks):
        for j in range(no_blocks):
            Empty_map[i][j] = Blocks(row= i,col = j,block_width=block_width)
    return Empty_map

def draw_map(win, map):
    row_map, col_map = map.shape
    for i in range(row_map):
        for j in range(col_map):
            map[i][j].draw(win)
    pygame.display.update()

def store(rmap):
    file = open('map.pkl','wb')
    pickle.dump(rmap,file)
    list_map = []
    for i in range(rmap.shape[0]):
        for j in range(rmap.shape[1]):
            rmap[i,j].add_state(list_map)

    with open("list_map.txt","w") as output:
        output.write(str(list_map))







def make_grid(rmap,save_grid = False):
    empty_grid = np.zeros((rmap.shape[0]*3,rmap.shape[1]*3))
    for i in range(rmap.shape[0]):
        for j in range(rmap.shape[1]):
            grid = rmap[i,j].add_to_grid(grid)
    if save_grid :np.save("map_grid",grid.T)  
    return grid.T







    

win = pygame.display.set_mode((win_width,win_width))
pygame.display.set_caption("Simulator_V0")

def main():
    file = open('map.pkl','rb')
    rmap = pickle.load(file)
    row = 0
    col = 0
    episode = True
    while episode:
        
        for ev in pygame.event.get():
            draw_map(win,rmap)
            if ev.type == pygame.QUIT:
                pygame.quit()
                episode = False
            if pygame.mouse.get_pressed()[0]: #LEFT_Click
                pos = pygame.mouse.get_pos()
                row, col = (pos[0]//block_width,pos[1]//block_width)
            if pygame.mouse.get_pressed()[1]:#RIGHT_Click
                pos = pygame.mouse.get_pos()
                rmap[pos[0]//block_width][pos[1]//block_width].change_type("void")
            #Change Type of the block  
            if ev.type == pygame.KEYDOWN:  
                if ev.key == pygame.K_i:
                    rmap[row,col].change_type("straight")
                    rmap[row,col].draw(win)
                if ev.key == pygame.K_l:
                    rmap[row,col].change_type("turn") 
                    rmap[row,col].draw(win)        
                if ev.key == pygame.K_t:  
                    rmap[row,col].change_type("T")
                    rmap[row,col].draw(win)
                if ev.key == pygame.K_p:    
                    rmap[row,col].change_type("plus")
                    rmap[row,col].draw(win)
                if ev.key == pygame.K_d:
                    rmap[row,col].change_type('void')
                    rmap[row,col].draw(win)
                #Move accros the map    
                if ev.key == pygame.K_UP:
                    if col-1 >= 0:
                        col -= 1
                if ev.key == pygame.K_DOWN:
                    if col+1 < win_width/block_width:
                        col +=1
                if ev.key == pygame.K_LEFT:
                    if row-1 >= 0:
                        row -= 1
                if ev.key == pygame.K_RIGHT:
                    if row+1 < win_width/block_width:
                        row += 1
                if ev.key ==pygame.K_s:
                    store(rmap)

                #Rotate The block
                if ev.key == pygame.K_r:
                    rmap[row][col].rotate()
                    rmap[row,col].draw(win)

                rmap[row,col].draw_pointer(win)


# main() 
        




        
