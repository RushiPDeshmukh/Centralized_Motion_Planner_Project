#!/usr/bin/env python3

import sys
import rospy
from std_msgs.msg import String
from car.srv import planner_srv, planner_srvResponse
#from car.msg import planner_msg, planner_msgResponse
class car_ros:
    def __init__(self):
        """
        Add ros init and stuff to generate car id if that is possible.
        
        
        """
        rospy.init_node('car_pub', anonymous=True)
        #self.car_id = ros.init_node('car', anonymous=True)   ... IDK if this is what we will need lets see...
        self.car_id = 0
        pass
        
    def car_client(self, start, end):
        rospy.wait_for_service('path_planner')
        try:
            self.path_planner = rospy.ServiceProxy('path_planner', planner_srv)
            self.response = self.path_planner(start, end)
            return self.response.path
        except rospy.ServiceException as e:
            print('service call failed : {}'.format(e))

    def car_publisher(self, x_pos, y_pos):
        self.pub = rospy.Publisher('car_simulator', String, queue_size=10)
        
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            car_info = self.car_id + ',' + x_pos + ',' + y_pos 
            self.pub.publish(car_info)
            rate.sleep()

if __name__ == "__main__":
    """
    TODO: Here take the numpy array and generate randomly the start and end points

    The lines written below can should be deleted once similar lines are implemented in get_path() function in car.py file.
    """
    x1, y1 = [0, 0] # get this randomly
    xf, yf = [0, 0]
    start = [x1, y1]
    end = [xf, yf]
    print('Requesting')
    car = car_ros()
    path = car.car_client(start,end)
    
    """TODO: Decide how to send this path further to the simulator"""
    """ 1. could just build the publisher subscriber right here, will check if I can make it possible."""



    