#!/usr/bin/env python

import click
import rospy
from geometry_msgs.msg import Twist


def turtalt():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('zolw')
    
    while not rospy.is_shutdown():
        twist = Twist()
	key_detected = click.getchar()

        up = rospy.get_param("up")
        left = rospy.get_param("left")
        right = rospy.get_param("right")
        down = rospy.get_param("down")


        if key == up :
            twist.linear.x=1.0
        if key == down :
            twist.linear.x=-1.0
        if key == left :
            twist.angular.z=1.0
        if key == right :
            twist.angular.z=-1.0

        pub.publish(twist)

if __name__ == '__main__':
    try:
        turtalt()
    except rospy.ROSInterruptException:
	pass