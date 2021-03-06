#!/usr/bin/env python3

from car.srv import planner_srv, planner_srvResponse
import rospy
import utils.a_star as a_star
import utils.centralized_planner as cp
class planner_ros:
    def __init__(self):
        rospy.init_node('planner_server_node')
        
        
    def handle_start_end(self, req):
        """
        This is the planner server
        This part of the code will handle the path planning
        Returns a variable array planned_path which contains the path

        TODO: Planning algorithm implementation to be called here on receiving 
        start and end node from the car as a request
        access : req.start and req.end
        start and end are a row 1x2 vector containg x,y coordinates
        """
        
        #self.planned_path = a_star.main(req.start,req.end)
        self.planned_path = cp.make_plan(req.start,req.end)
        path_x, path_y, car_id, time = self.planned_path[:,0], self.planned_path[:,1],self.planned_path[:,2], self.planned_path[:,3]
        if path_x is not None:
            print('Path found successfully')
        # print(path_x)
        #path_x, path_y = planner_srvResponse(self.planned_path) 
        return path_x, path_y

    def send_start_end(self):
        s = rospy.Service('path_planner', planner_srv, self.handle_start_end)
        print('The planner server is ready to plan')
        rospy.spin()

if __name__ == "__main__":
    planner = planner_ros()
    planner.send_start_end()
