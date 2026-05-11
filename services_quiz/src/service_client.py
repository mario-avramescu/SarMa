#!/usr/bin/env python

import rospy
from services_quiz.srv import Sarma

rospy.init_node('client_srv')
rospy.wait_for_service('/move_robot')

service = rospy.ServiceProxy('/move_robot', Sarma)
side = float(input('Distance: '))
repetitions = int(input('Repetitions:'))
result = service(side, repetitions)

print (result.success)

