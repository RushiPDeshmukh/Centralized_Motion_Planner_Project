import rospy
from std_msgs.msg import String


class simulator_ros:
    def __init__(self):
        rospy.init_node('simulator', anonymous=True)
    
    def car_callback(self, data):
        """
        TODO:: Add whatever you have for simulating the car here...
        does whatever necessary with the data received from car data.
        """

        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    def car_sub(self):
        """
        Subscribes to car publisher where we are getting the data
        """
        rospy.Subscriber('car_simulator', String, self.car_callback)

        rospy.spin()

if __name__ == "__main__":
    """
    TODO:: Add whatever necessary to simulate in pygame
    """
    
    sim_ros = simulator_ros()
    sim_ros.car_sub()