#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster, TransformStamped
from std_msgs.msg import Float32

class StatePublisher(Node):
    def __init__(self):
        super().__init__('state_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'traj_test',
            self.listener_callback,
            10)
        self.subscription

        self.odom_trans = TransformStamped()
        self.odom_trans.header.frame_id = 'odom'
        self.odom_trans.child_frame_id = 'base_link'

        qos_profile = QoSProfile(depth=10)
        self.joint_pub = self.create_publisher(JointState, 'joint_states', qos_profile)
        self.broadcaster = TransformBroadcaster(self, qos=qos_profile)

        self.joint_state = JointState()

    def listener_callback(self, msg):
        now = self.get_clock().now()
        self.joint_state.header.stamp = now.to_msg()

        self.odom_trans.header.stamp = now.to_msg()
        self.odom_trans.transform.rotation.z = msg.data

        self.joint_pub.publish(self.joint_state)
        self.broadcaster.sendTransform(self.odom_trans)

def main(args=None):
    rclpy.init(args=args)
    node = StatePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    