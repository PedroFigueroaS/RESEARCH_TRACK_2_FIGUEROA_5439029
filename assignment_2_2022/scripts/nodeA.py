#!/usr/bin/env python

"""
.. module:: nodeA
   :platform: Unix
   :synopsis: Set and cancel a goal

.. moduleauthor:: Pedro Figueroa <lan.fig.pf@gmail.com>

"""



#Import the requires libraries, function, and files
from __future__ import print_function
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

import actionlib
import actionlib_msgs
import assignment_2_2022.msg



def new_position():
   """
   In **new_position** function, the program ask to enter the new goal by entering a position in X and Y axes. Then 
   this values goes to the goal properties using the PoseStamped message type. Finally, the client value uses the function send_goal
   to send the position to the Action server. After a pause of 2 seconds, the program returns to the **user_select()** function.
   """
   global client #use the same client object created in the main function to connect the action client
 
 
   client.wait_for_server() #wait to connect to the server
   goal=PoseStamped() #define the goal according to the features in PoseStamped
   xpos=input('\nEnter posx: ')
   ypos=input('\nEnter posy: ')
 #input the target (x,y) and assign it to the goal
   goal.pose.position.x=int(xpos)
   goal.pose.position.y=int(ypos)
   goal = assignment_2_2022.msg.PlanningGoal(goal)
 #send the new goal to the client server
   client.send_goal(goal)
   rospy.sleep(2)


 #return to the user interface
   user_select()

def cancel_sim():
   """
   In the **cancel_sim** function, the client call the cancel_goal function to stop the robots movement
   and cancel the current goal. Finally moves back to **user_select()**
   """
 #client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction)
   client.cancel_goal()#send a signal to cancel the action of reaching the new target
   print("goal cancelled: going back to user select...")
   user_select() #send the new goal to the client server

def user_select():
   """
   In the **user_select** function, the program ask to choose for 1 option: 1 to set a new goal, 2 to cancel the current goal and stop
   the robot. Based in the option, the program then will move to the functions **new_position** or **cancel_sim**
   """
   
   op=input("choose action: ")#enter the desired option
 

   if(op=="1"): #if set new target, go to new_position()
      new_position()
   elif(op=="2"):
      cancel_sim()#if cancel the target, go to cancel_sim()
#Main program
def main():
   """
   Main function of nodeA.py. Displays the options for the user to set a new goal or cancel the current goal
   Then creates a new topic **nodeAclient**, then creates a client variable to use the Action Client */reaching_goal*.
   Finally, call the function **user_select()**
   """
       #option for the user
   global client
   print("1: define position")
   print("2: cancel")
   rospy.init_node('nodeAclient')  # Initializes a rospy node
        
   client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction)#create a client object for an Action client related to the message files Planning.action
        
   user_select()#enter to the main user interface

if __name__ == '__main__':
   main()