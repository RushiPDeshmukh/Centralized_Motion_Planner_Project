import roslaunch
import rospy
for i in range(5):

    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, ["../launch/car.launch"])
    launch.start()
    try:
      launch.spin()
    finally:
      launch.shutdown()