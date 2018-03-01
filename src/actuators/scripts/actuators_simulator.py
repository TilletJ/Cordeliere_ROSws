#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python version 2.7

"""
    --- Actuators_simulator ---

Summary:

I/O:

# TODO:
- Use the unity
"""

import rospy
from geometry.msg import Twist


def callbackCommand(data):
    """ Callback function activated when a data is received from the IMU
    """
    global cmd
    # TODO: change this to have something in relation with the physical configuration of the AUV
    cmd.linear = data.linear
    cmd.angular = cmd.angular


if __name__ == '__main__':
    """ Main program
    """

    # ------------- INITIALIZATION -------------

    rospy.init_node('actuators_simulator', anonymous=True)
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rate = rospy.Rate(10)  # frenquency in Hertz

    # Initialization:
    cmd = Twist()

    # Subscribers:
    rospy.Subscriber("command_msg", Twist, callbackCommand)
    pub = rospy.Publisher('actuators_command', Twist, queue_size=1)
    # ------------------ LOOP ------------------

    while not rospy.is_shutdown():

        # Sending data:
        pub.publish(cmd)

        rate.sleep()