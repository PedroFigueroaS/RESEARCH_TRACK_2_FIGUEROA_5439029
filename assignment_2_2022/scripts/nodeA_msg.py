#!/usr/bin/env python

"""
.. module:: nodeA_msg
   :platform: Unix
   :synopsis: Publish the positions and velocities in a different topic

.. moduleauthor:: Pedro Figueroa <lan.fig.pf@gmail.com>

"""

import rospy
from geometry_msgs.msg import Point, Pose, Twist
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import math
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from tf import transformations
from std_srvs.srv import *
import time
from assignment_2_2022.msg import node_pub 

# Brings in the SimpleActionClient
import actionlib
import actionlib_msgs
import assignment_2_2022.msg


def msg_callback(info):
    
    """
   In the **msg_callback** function, a publisher is created, to publish value in the topic *chatter*, using node_pub custom message.
   The values store in the *info* variable are related with the current position and velocity of the robot. They will be stored
   in the **message** variable that has the attibutes of node_pub custom message. Finally this message will be displayed and published.
   """
    
    pub = rospy.Publisher('chatter', node_pub, queue_size=10)#create pub object to publish in the nodeA
 #while not rospy.is_shutdown():
    message=node_pub()#message will have the properties of the nodeA() msg
    message.x=info.pose.pose.position.x
    message.y=info.pose.pose.position.y
    message.velx=info.twist.twist.linear.x
    message.vely=info.twist.twist.linear.y
 
 #in message assign the position and velocity in (X,Y) each time in the simulation
 
    print(message)
    rate = rospy.Rate(20) # Set a publish rate
    pub.publish(message) #publish in the topic nodeA
    rate.sleep()
  
def main():
    """
   Main function of nodeA_msg. The program create a node **nodeAmsg**. It subscribes to the topic */odom*, and call the function
   msg_callback. Due to issues between sphinx behaviour and this code, line 24 of the program has been commented: 
   **from assignment_2_2022.msg import node_pub**. To run this code erase the **#** character behind the line. 
   """
    rospy.init_node('nodeAmsg')
    rospy.Subscriber("/odom", Odometry, msg_callback)#subscribe to the topic /odom, and call the function msg_callback
    rospy.spin()#keep the program working until the .py finishes
#main program
if __name__ == '__main__':
   main()
