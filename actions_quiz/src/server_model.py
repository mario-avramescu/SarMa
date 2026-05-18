#! /usr/bin/env python

import rospy
import actionlib
from std_msgs.msg import Empty
from actions_quiz.msg import SarmaFeedback, SarmaResult, SarmaAction

# import your custom messages

class DroneClass(object):
    
  # create messages that are used to publish feedback/result
  _feedback = SarmaFeedback()
  _result   = SarmaResult()

  def __init__(self):
    # creates the action server
    self._as = actionlib.SimpleActionServer("drone_action", SarmaAction, self.goal_callback, False)
    self._as.start()

    self._pub_takeoff = rospy.Publisher("/ardrone/takeoff", Empty, queue_size=1)
    self._pub_land = rospy.Publisher("/ardrone/land", Empty, queue_size=1)
    
  def goal_callback(self, goal):
    # this callback is called when the action server is called
    rate = rospy.Rate(1)
    command_sarma = goal.goal

    if command_sarma == "TAKEOFF":
      self._pub_takeoff.publish(Empty())
      self._feedback.feedback = "TAKEOFF"

      while rospy.is_shutdown():
        if self._as.is_preempt_requested():
          self._as.set_preempted()
          break

        self._as.publish_feedback(self._feedback)
        rate.sleep(1)

    elif command_sarma == "LAND":
      self._pub_takeoff.publish(Empty())
      self._feedback.feedback = "LAND"

      while rospy.is_shutdown():
        if self._as.is_preempt_requested():
          self._as.set_preempted()
          break

        self._as.publish_feedback(self._feedback)
        rate.sleep(1)

    self._as.set_succeeded(self._result)
      
if __name__ == '__main__':
  rospy.init_node('drone_server')
  DroneClass()
  rospy.spin()