
import math
import numpy as np
import matplotlib.pyplot as plt
import os

show_animation = True
# show_animation = False

class AStarPlanner:

    def __init__(self):
        """
        Initialize grid map for a star planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """
        map_path = '//utils//grid_map.npy'
        dir_path = os.path.abspath(os.path.dirname(__file__))
        path = dir_path + map_path
        self.map_array =  np.load(path)

        self.resolution = 1
        self.rr = 0
        self.min_x, self.min_y = 0, 0
        self.obstacle_map = self.map_array.astype(np.int32).tolist()
        self.ox,self.oy = obstacles(self.map_array)
        self.max_x, self.max_y =  self.map_array.shape[0], self.map_array.shape[1]
        self.x_width, self.y_width = 1, 1
        self.motion = self.get_motion_model()
        self.calc_obstacle_map(self.ox, self.oy)

    class Node:
        def __init__(self, x, y, cost, parent_index):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, S, G):
        """
        A star path search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gy: goal y position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """
        sx = S[0]
        sy = S[1]
        gx = G[0]
        gy = G[1]

        start_node = self.Node(self.calc_xy_index(sx, self.min_x),
                               self.calc_xy_index(sy, self.min_y), 0.0, -1)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x),
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict()
        open_set[self.calc_grid_index(start_node)] = start_node

        while 1:
            if len(open_set) == 0:
                print("Could not find path :(")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(goal_node,
                                                                     open_set[
                                                                         o]))
            current = open_set[c_id]

            # show graph
            if show_animation:  # pragma: no cover
                plt.plot(self.calc_grid_position(current.x, self.min_x),
                         self.calc_grid_position(current.y, self.min_y), "xc")
                # for stopping simulation with the esc key.
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event: [exit(
                                                 0) if event.key == 'escape' else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

            if current.x == goal_node.x and current.y == goal_node.y:
                # print("Found goal")
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion):
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2], c_id)
                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)

        return rx, ry

    def calc_final_path(self, goal_node, closed_set):
        # generate final course
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)]
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index
        rx_s2g = np.flip(rx)
        ry_s2g = np.flip(ry)
        return rx_s2g, ry_s2g

    @staticmethod
    def calc_heuristic(n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        return d

    def calc_grid_position(self, index, min_position):
        """
        calc grid position

        :param index:
        :param min_position:
        :return:
        """
        pos = index * self.resolution + min_position
        return pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x)

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False

        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):
        pass
        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)

        # obstacle map generation
        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)]

        for ix in range(self.x_width):
        #     x = self.calc_grid_position(ix, self.min_x)
            for iy in range(self.y_width):
        #         y = self.calc_grid_position(iy, self.min_y)
                if self.map_array[ix,iy] == 0:
                    self.obstacle_map[ix][iy] = True
        #         for iox, ioy in zip(ox, oy):
        #             d = math.hypot(iox - x, ioy - y)
        #             if d <= self.rr:
        #                 self.obstacle_map[ix][iy] = True
        #                 break

    @staticmethod
    def get_motion_model():
        # dx, dy, cost
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1]]
                #   [-1, -1, math.sqrt(2)],
                #   [-1, 1, math.sqrt(2)],
                #   [1, -1, math.sqrt(2)],
                #   [1, 1, math.sqrt(2)]]

        return motion


def obstacles(map_array):
    ox = []
    oy = []
    O = np.argwhere(map_array<1)
    ox = O[:,0].astype(np.int32).tolist()
    oy = O[:,1].astype(np.int32).tolist()

    # # add boundaries if the space is open
    # min_x = -1
    # min_y = -1
    # max_x = map_array.shape[0] + 1
    # max_y = map_array.shape[1] + 1 
    # for i in range(min_x, max_x):
    #     ox.append(i)
    #     oy.append(min_y)
    # for i in range(min_x, max_x):
    #     ox.append(i)
    #     oy.append(max_y)
    # for i in range(min_y, max_y):
    #     ox.append(min_x)
    #     oy.append(i)
    # for i in range(min_y, max_y):
    #     ox.append(max_x)
    #     oy.append(i)
    
    return ox,oy



def main(S,G):
    a_star = AStarPlanner()
    
    if show_animation:  # pragma: no cover
        plt.plot(a_star.ox, a_star.oy, ".k")
        plt.plot(S[0], S[1], "og")
        plt.plot(G[0], G[1], "xb")
        # plt.grid(True)
        plt.axis("equal")
    rx, ry = a_star.planning(S,G)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-r")
        plt.pause(0.001)
        plt.show()
    
    path_x = np.array(rx)
    path_y = np.array(ry)
    # np.save('path1',path)
    return path_x, path_y

if __name__ == '__main__':
    S = [60,14]  # [m]
    G = [17,6]  # [m]

    main(S,G)
    # main(gx,gy,sx,sy)
    
    # import time
    # tic = time.time()
    # for i in range(50):
    #     main(sx,sy,gx,gy)
    #     main(gx,gy,sx,sy)
    #     print(2*i)
    # toc = time.time()
    # print('Time for 100 searches:',np.round(toc-tic))