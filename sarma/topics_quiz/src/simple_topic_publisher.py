#! /usr/bin/env python

import rospy                              			
from std_msgs.msg import Int32      
from geometry_msgs.msg import Twist	

rospy.init_node('topic_publisher')         		
pub = rospy.Publisher('/cmd_vel', Int32, queue_size=1)    	
			                                           

rate = rospy.Rate(2)                       			
                           			                             			

while not rospy.is_shutdown():             		
	
