#!/usr/bin/env python

"""
.. module:: nodeB
   :platform: Unix
   :synopsis: Count the number of reached and cancelled goals

.. moduleauthor:: Pedro Figueroa <lan.fig.pf@gmail.com>

"""

import rospy

import time
from std_srvs.srv import Empty, EmptyResponse
import assignment_2_2022.msg

ncancelled=0
nreached=0

def serv_callback(req):#service function
   """
   In the **serv_callback** function, when the service is called, the program will display the number of targets cancelled
   and reached
   """
   global ncancelled , nreached
   print("number of targets cancelled: \n",ncancelled)
   print("number of targets reached: \n",nreached)
   #print the number of times the goal is reached and cancelled 
   return EmptyResponse()


def cllback(msg):#subscriber function
   """
   In the **cllback** function, each time the robot reach or cancel a goal, the msg variable will make its property *status* 
   change to 2 or 3. Depending on the value, a counter for each case will increase its value.
   """
   global ncancelled 
   global nreached
   if (msg.status.status==2):#each time a goal es cancelled, 
    
      ncancelled=ncancelled+1
   elif (msg.status.status==3):
    
      nreached=nreached+1

#main function
def main():
   """
   Main function of nodeB.py. Creates the node *nodeB*, subscribes to the topic */reaching_goal/result*, and call the **cllback**
   function. Call the service "reach_cancel_ints", and calls the **serv_callback** function. The program keeps running with the
   rospy.spin function. 
   """
   
   # Initializes a rospy node
   rospy.init_node('nodeB')
   rospy.Subscriber("/reaching_goal/result",assignment_2_2022.msg.PlanningActionResult,cllback)#subsrcibe to the topic /reaching_goal and call the cllback function
   rospy.Service("reach_cancel_ints",Empty,serv_callback)#call the service "reach_cancel_ints" and call the serv_callback() function
   rospy.spin()#keep the program working until python terminates it

if __name__ == '__main__':
   main()