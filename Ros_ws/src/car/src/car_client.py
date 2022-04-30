#!/usr/bin/env python3
import utils.car_gen as car_gen
import sys
import random
import rospy
from car.msg import sim_msg
from std_msgs.msg import Int64MultiArray
from car.srv import planner_srv, planner_srvResponse
#from car.msg import planner_msg, planner_msgResponse
class car_ros:
    def __init__(self):
        """
        Add ros init and stuff to generate car id if that is possible.
        
        
        """
        rand_id = random.randint(0,1000)

        node_name = 'car_' + str(rand_id)
        rospy.init_node(node_name, anonymous=True)
        #self.car_id = ros.init_node('car', anonymous=True)   ... IDK if this is what we will need lets see...
        self.car_id = rand_id
        
        
    def car_client(self, start, end):
        rospy.wait_for_service('path_planner')
        try:
            self.path_planner = rospy.ServiceProxy('path_planner', planner_srv)
            self.response = self.path_planner(start, end)
            return [self.response.path_x, self.response.path_y]
        except rospy.ServiceException as e:
            print('service call failed : {}'.format(e))

    def car_publisher(self, path_x, path_y):
        self.pub = rospy.Publisher('car_simulator', sim_msg, queue_size=10)
        
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            car_info = None 
            for i in range(len(path_x)):
                x_pos = path_x[i]
                y_pos = path_y[i]
                #print(x_pos, y_pos)
                self.pub.publish(self.car_id,x_pos,y_pos)
                rate.sleep()
            break     
            
        
if __name__ == "__main__":
    """
    TODO: Here take the numpy array and generate randomly the start and end points

    The lines written below can should be deleted once similar lines are implemented in get_path() function in car.py file.
    """
    start,end = car_gen.main()
    print('Requesting')
    car = car_ros()
    path_x, path_y = car.car_client(start,end)
    print(path_x, path_y)
    try:
        car.car_publisher(path_x, path_y)
    except rospy.ROSInterruptException:
        pass


    