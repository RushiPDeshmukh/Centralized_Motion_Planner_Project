#!/usr/bin/env python3
import rospy
from car.msg import sim_msg
from std_msgs.msg import Int64
from utils.simulator import *

map_path = '//utils//map.pkl'
dir_path = os.path.abspath(os.path.dirname(__file__))
path = dir_path + map_path
file = open(path,'rb')
rmap =  pickle.load(file)

class simulator_ros:
    def __init__(self):
        rospy.init_node('simulator', anonymous=True)
    
    def car_callback(self, data):
        """
        TODO:: Add whatever you have for simulating the car here...
        does whatever necessary with the data received from car data.
        """
        #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        data_tuple = (data.x_pos, data.y_pos,data.car_id,0)
        my_tuple = []
        my_tuple.append(data_tuple)
        render(win, rmap, my_tuple, car_list)
        

    def car_sub(self):
        """
        Subscribes to car publisher where we are getting the data
        """
        rospy.Subscriber('car_simulator', sim_msg, self.car_callback)

        rospy.spin()

if __name__ == "__main__":
    """
    TODO:: Add whatever necessary to simulate in pygame
    """
    

    sim_ros = simulator_ros()
    sim_ros.car_sub()