#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import std_msgs.msg as stdmsg

if __name__ == '__main__':
    rospy.init_node('tf_to_topic')

    listener = tf.TransformListener()
    pub = rospy.Publisher('orientation', stdmsg.Float32, queue_size=10)
    rate = rospy.Rate(25.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('odom', 'duro', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        #print(rot)
        euler = tf.transformations.euler_from_quaternion(rot)
        roll = euler[0]
        pitch = euler[1]
        yaw = euler[2]
        pub.publish(yaw) # * 180 / math.pi
        rate.sleep()