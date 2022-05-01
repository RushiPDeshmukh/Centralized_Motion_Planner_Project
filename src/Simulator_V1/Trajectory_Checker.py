import numpy as np

def is_valid(path,path_bank):
    collision_points = []
    validity = True
    for state in path:
        for row in path_bank:
            # print('state',state)
            if row[0] == state[0] and row[1] == state[1] and row[3] == state[3]:
                validity = False
                collision_points.append(list(state))
    return validity,collision_points

def correct_paths(path, path_bank):
    valid = False
    curr_path = path
    count = 0
    valid,collision_points = is_valid(curr_path,path_bank)
    while not valid and count !=5:
        valid,collision_points = is_valid(curr_path,path_bank)
        count+=1
        for state in collision_points:
            t = state[3]
            path[path[:,3]>=t] = path[path[:,3]>=t] + 1
    return path,valid,collision_points
    

