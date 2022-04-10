#!/usr/bin/env python3

from car.srv import planner_srv, planner_srvResponse
import rospy

def handle_start_end(req):
    """
    This is the planner server
    This part of the code will handle the path planning
    Returns a variable array planned_path which contains the path

    TODO: Planning algorithm implementation to be called here on receiving 
    start and end node from the car as a request
    access : req.start and req.end
    start and end are a row 1x2 vector containg x,y coordinates
    """
    
    planned_path =[]
    return planner_srvResponse(planned_path)

def send_start_end():
    rospy.init_node('planner_server_node')
    s = rospy.Service('path_planner', planner_srv, handle_start_end)
    print('The planner server is ready to plan')
    rospy.spin()

if __name__ == "__main__":
    send_start_end()
