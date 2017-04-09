#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Adapted to Arabic by adding libraries in espeak-data in 
# /usr/lib/lib-arm...../espeak-data
# how to test  :
# rosrun slp_espeakerv1 speaker.py  in one terminal
# rostopic pub /recognizer/output /std_msgs/String "السلام عليكم" -v mb-ar1  in another terminal
# rostopic pub /recognizer/output /std_msgs/String "السلام عليكم" -v ar 


PKG = 'espeak_asl'

# Same as typing this:  espeak -v english "whatever the text is"
# into the terminal
# All ROS python nodes should have these lines
import roslib; 
roslib.load_manifest(PKG)
import rospy

# This loads the definition of the service (Say.srv)
from std_msgs.msg import String
# This is needed to execute commands in the shell
import subprocess

# You can call the service from the command line with something like:
'''
 1  ar              --/M      arabic-mbrola-1    mb/mb-ar1            
 2  ar              --/M      arabic-mbrola-2    mb/mb-ar2            
 5  ar              --/M      arabic             ar                   
 5  ar              --/M      arabic             ar-fm                
 5  ar              --/M      mohamed            ar_moh               
 5  ar              --/M      mostafa            ar_mostafa        
'''
# rosservice call /say "Hello World"
class Speaker():
    def __init__(self):
        rospy.init_node('speaker', anonymous=True)
        rospy.loginfo("Say one of the Sign commands...")
        # Subscribe to the recognizer output and set the callback function
        rospy.Subscriber('/speak_ar', String, self.handle_say_ar)
        rospy.Subscriber('/speak_mb_ar1', String, self.handle_say_mb_ar1)
        rospy.Subscriber('/speak_mb_ar2', String, self.handle_say_mb_ar2)
        rospy.Subscriber('/speak_ar_fm', String, self.handle_say_ar_fm)
        rospy.Subscriber('/speak_ar_moh', String, self.handle_say_ar_moh)
        rospy.Subscriber('/speak_ar_mostafa', String, self.handle_say_ar_mostafa)

    def handle_say_ar(self, msg):
        rospy.loginfo(msg.data)
        subprocess.call(["espeak", "-v", "ar", msg.data]) 
        return []

    def handle_say_mb_ar1(self, msg):
        rospy.loginfo(msg.data)
        subprocess.call(["espeak", "-v", "mb-ar1", msg.data]) 
        return []

    def handle_say_mb_ar2(self, msg):
        rospy.loginfo(msg.data)
        subprocess.call(["espeak", "-v", "mb-ar2", msg.data]) 
        return []

    def handle_say_ar_fm(self, msg):
        rospy.loginfo(msg.data)
        subprocess.call(["espeak", "-v", "ar-fm", msg.data]) 
        return []

    def handle_say_ar_moh(self, msg):
        rospy.loginfo(msg.data)
        subprocess.call(["espeak", "-v", "ar_moh", msg.data]) 
        return []

    def handle_say_ar_mostafa(self, msg):
        rospy.loginfo(msg.data)
        subprocess.call(["espeak", "-v", "ar_mostafa", msg.data]) 
        return []


if __name__ == '__main__':
    try:
        speaker = Speaker()
        rospy.spin()
    except rospy.ROSInterruptException: pass


##  espeak -v mb-ar1   "السلام عليكم"
