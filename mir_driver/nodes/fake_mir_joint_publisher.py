#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState

def fake_mir_joint_publisher():
    rospy.init_node('fake_mir_joint_publisher')
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    try:
        tf_prefix = rospy.get_param(rospy.get_namespace() + 'tf_prefix')
    except Exception as e:
        rospy.logwarn('Exception happened'.format(e))
        tf_prefix = ''
    
    r = rospy.Rate(50.0)
    while not rospy.is_shutdown():
        js = JointState()
        js.header.stamp = rospy.Time.now()
        js.name =  [tf_prefix + 'left_wheel_joint', tf_prefix + 'right_wheel_joint',
                    tf_prefix + 'fl_caster_rotation_joint', tf_prefix + 'fl_caster_wheel_joint',
                    tf_prefix + 'fr_caster_rotation_joint', tf_prefix + 'fr_caster_wheel_joint',
                    tf_prefix + 'bl_caster_rotation_joint', tf_prefix + 'bl_caster_wheel_joint',
                    tf_prefix + 'br_caster_rotation_joint', tf_prefix + 'br_caster_wheel_joint']
        js.position = [0.0 for _ in js.name]
        js.velocity = [0.0 for _ in js.name]
        js.effort = [0.0 for _ in js.name]
        pub.publish(js)
        r.sleep()


if __name__ == '__main__':
    try:
        fake_mir_joint_publisher()
    except rospy.ROSInterruptException:
        pass
