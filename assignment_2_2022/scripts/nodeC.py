#!/usr/bin/env python

"""
.. module:: nodeC
   :platform: Unix
   :synopsis: Subsribes to the chatter topic and display the total distance and velocity between the robot and the goal

.. moduleauthor:: Pedro Figueroa <lan.fig.pf@gmail.com>

"""


import rospy
import math
from assignment_2_2022.msg import node_pub
from geometry_msgs.msg import Point, Pose, Twist
from geometry_msgs.msg import PoseStamped


euc_dist=0
euc_vel=0
def callback(msg):
    """
    The **callback** function request the goal position from the parameters of the project, and the current position from the msg variable
    that contains the current position and velocity attributes. By computing the euclidean formula to the difference of the desired
    and current position and for the velocities, it is computed and displayes the total distance and velocity 
    between the robot and the goal.
    """
#while not rospy.is_shutdown():
    pxd=rospy.get_param("/des_pos_x")
    pyd=rospy.get_param("/des_pos_y")
    #get the target position from the rospy parameters
    px=msg.x
    py=msg.y
    velx=msg.velx
    vely=msg.vely
    #get the posx, posy, velx, vely from the msg object
    euc_dist=math.sqrt(((pxd-px)**2)+((pyd-py)**2))#compute the euclidean distance
    euc_vel=math.sqrt(((velx)**2)+((vely)**2))#compute the euclidean velocity
    print("Distance:",euc_dist, end=" ")#print the distance
    print("velx:",euc_vel)#print the velocity

def main():
    """
    Main function of nodeC.py. Creates a node *nodeC*, then it subscribes to the topic *chatter* and call the **callback** function 
    """
    # Initializes a rospy node
    rospy.init_node('nodeC')
    rospy.Subscriber("chatter", node_pub, callback)#subscribe to the chatter topic, with the type of message of nodeA, and call the callback function
    rospy.spin()#keep the program working until python terminates it

#main function
if __name__ == '__main__':
    main()

