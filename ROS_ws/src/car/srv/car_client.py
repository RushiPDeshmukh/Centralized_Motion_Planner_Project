#!/usr/bin/env python3

import sys
from urllib import response
import rospy
from car.srv import *
from car.msg import planner_msg, planner_msgResponse

def car_client(start, end):
    rospy.wait_for_service('path_planner')
    try:
        path_planner = rospy.ServiceProxy('path_planner', planner_msg)
        response = path_planner(start, end)
        return response.path
    except rospy.ServiceException as e:
        print('service call failed : {}'.format(e))

if __name__ == "__main__":
    """
    TODO: Here take the numpy array and generate randomly the start and end points
    """
    x1, y1 = [0, 0] # get this randomly
    xf, yf = [0, 0]
    start = [x1, y1]
    end = [xf, yf]
    print('Requesting')
    path = car_client(start,end)
    
    """TODO: Decide how to send this path further to the simulator"""
    """ 1. could just build the publisher subscriber right here, will check if I can make it possible."""