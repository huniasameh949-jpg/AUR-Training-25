#! usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32 , Int64
from random import randint

class DistancePub(Node):
    def __init__(self):
        super().__init__('distance_node')
        self.get_logger().info(f"publisher distance started")
        self.distancepub=self.create_publisher(Int64,'test_topic2',10)
        self.timer=self.create_timer(1.0,self.callback_distance)

    def callback_distance(self):
        msg=Int64()
        msg.data=randint(0,1000)
        self.distancepub.publish(msg)
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node=DistancePub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
        