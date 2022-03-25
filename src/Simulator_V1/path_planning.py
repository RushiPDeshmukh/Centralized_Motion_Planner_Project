import numpy as np
import matplotlib.pyplot as plt
import pygame
class path_plan():
    def __init__(self, car, map):
        """
        Takes in the car object and the map object to calculate the path for the car in the map given.
        """
        self.car = car
        self.map = map
    
    def get_start_end(self):
        self.start_end_nodes = []
        # If it is a house or a complex it can be a start or end node for the car.
        # Looping over the map to get start and end node
        for i in self.map:
            if i.rtype == 'house':
                self.start_end_nodes.append(i)
            if i.rtype == 'complex':
                self.start_end_nodes.append(i)
            else:
                pass
        #return self.start_end_nodes
        
    def is_road(node):
        if node.rtype == 'road':
            return True
        else:
            return False

    def add_neighbours(self):
        self.neighbours = []
        #We need to know current car directon too to check if it is going in the right direction. ?????????
        if self.row < self.total_rows - 1 and self.is_road(self.map[self.row + 1][self.col]): # DOWN
            if self.map[self.row + 1][self.col].dir == 'down':
                self.neighbors.append(self.map[self.row + 1][self.col])
        
        
        if self.row > 0 and self.is_road(self.map[self.row - 1][self.col]): # UP
            if self.map[self.row - 1][self.col].dir == 'up':
                self.neighbors.append(self.map[self.row - 1][self.col])
        
        
        if self.col < self.total_rows - 1 and self.is_road(self.map[self.row][self.col + 1]): # RIGHT
            if self.map[self.row][self.col + 1].dir == 'right':
                self.neighbors.append(self.map[self.row][self.col + 1])
        
        
        if self.col > 0 and not self.is_road(self.map[self.row][self.col - 1]): # LEFT
            if self.map[self.row][self.col - 1].dir == 'left':
                self.neighbors.append(self.map[self.row][self.col - 1])

    