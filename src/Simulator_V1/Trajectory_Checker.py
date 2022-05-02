import numpy as np

def is_valid(path,path_bank):
    collision_points = []
    validity = True
    for state in path:
        for row in path_bank:
            # print('state',state)
            if (row[0] == state[0] and row[1] == state[1] and row[3] == state[3] and row[2]!=state[2]):
                validity = False
                collision_points.append(list(state))
    return validity,collision_points

def correct_paths(path, path_bank):
    valid = False
    curr_path = path
    count = 0
    valid,collision_points = is_valid(curr_path,path_bank)
    while not valid and count !=5:
        for state in collision_points:
            t = state[3]
            prev_state = curr_path[curr_path[:,3]==t-1]
            curr_path[curr_path[:,3]>=t,3] = curr_path[curr_path[:,3]>=t,3] + 1
            curr_path = np.append(curr_path,prev_state)
            curr_path = np.reshape(curr_path,(-1,4))
            curr_path = curr_path[curr_path[:,3].argsort()].astype(np.int16)
        valid,collision_points = is_valid(curr_path,path_bank)
        count+=1

    return path,valid,collision_points
    

