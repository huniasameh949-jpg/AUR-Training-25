#! usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from random import randint

class SpeedPub(Node):
    def __init__(self):
        super().__init__('speed_node')
        self.get_logger().info(f"publisher speed started")
        self.speedpub=self.create_publisher(Int32,'test_topic1',10)
        self.timer=self.create_timer(1.0,self.callbackspeed)

    def callback_speed(self,msg):
        msg=Int32
        msg.data=randint(0,300)
        self.speedpub.publish(msg)
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node=SpeedPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
        