#!/usr/bin/env python

import rospy
from services_quiz.srv import Sarma
from geometry_msgs.msg import Twist 

rospy.init_node('server_srv')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

cmd = Twist()
rate = rospy.Rate(1)

def move(linear_x = 0.0, angular_z = 0.0, side = 0):
    cmd.linear.x = linear_x
    cmd.angular.z = angular_z

    if side !=0:
        end_time = rospy.Time.now() + rospy.Duration(side)

        while rospy.Time.now() < end_time:
            pub.publish(cmd)
            rate.sleep()

    stop_cmd = Twist()
    pub.publish(stop_cmd)
    rospy.sleep(0.5)

def callback(request):

    repetitions = request.repetitions
    side = request.side

    for i in range(0, repetitions):
        for i in range(0, 3): #patrat 
            move(linear_x=0.1, side=side)
            move(angular_z=0.1)

    return True


service_srv = rospy.Service('/move_robot', Sarma, callback)
rospy.spin()
