import numpy as np

def is_valid(path,path_bank):
    collision_points = []
    validity = True
    for state in path:
        if state in path_bank:
            validity = False
            collision_points.append(state)
    return validity,collision_points

def correct_paths(path, path_bank):
    valid = False
    curr_path = path
    while not valid:
        valid,collision_points = is_valid(curr_path,path_bank)
        
