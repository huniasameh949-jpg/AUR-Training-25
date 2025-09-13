#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim_msgs.srv import Spawn, Kill
from turtlesim_msgs.msg import Pose
from std_msgs.msg import Int32
import random
import math

class TurtleChase(Node):
    def __init__(self):
        super().__init__('turtle_chase')
       
        self.score_publisher = self.create_publisher(Int32, '/score_topic', 10)
        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.kill_client = self.create_client(Kill, '/kill')

        self.player_position = None
        self.enemies_position = {}                
        self.enemies_names = ['enemy1', 'enemy2', 'enemy3']
        self.enemies_subscriber = {}

        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn service...')
        while not self.kill_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /kill service...')

        self.create_subscription(Pose, '/turtle1/pose', self.player_callback, 10)

        for name in self.enemies_names:
           
            self.enemies_subscriber[name] = self.create_subscription(
                Pose,
                f'/{name}/pose',
                lambda msg, n=name: self.enemy_callback(msg, n),
                10
            )
           
            self.spawn_enemy(name)

        self.score = 0
        self.create_timer(0.1, self.check_collision)

        self.get_logger().info('Turtle Chase node started.')

    def player_callback(self, msg: Pose):
        self.player_position = msg

    def enemy_callback(self, msg: Pose, name: str):
        self.enemies_position[name] = msg

    def spawn_enemy(self, name: str):
        req = Spawn.Request()
        req.x = random.uniform(0.5, 10.5)
        req.y = random.uniform(0.5, 10.5)
        req.theta = random.uniform(0, 2 * math.pi)
        req.name = name
        future = self.spawn_client.call_async(req)

        def done_callback(fut):
            try:
                res = fut.result()
               
                self.get_logger().info(f"Spawned {name} at ({req.x:}, {req.y:})")
            except Exception as e:
                self.get_logger().error(f"Failed to spawn {name}: {e}")

        future.add_done_callback(done_callback)

    def kill_enemy(self, name: str, respawn: bool = True):
        req = Kill.Request()
        req.name = name
        future = self.kill_client.call_async(req)

        def done_callback(fut):
            try:
                fut.result()
                self.get_logger().info(f"Killed {name}")

                if respawn:
                    self.spawn_enemy(name)
            except Exception as e:
                self.get_logger().error(f"Failed to kill {name}: {e}")

        future.add_done_callback(done_callback)

    def find_distance(self, p1: Pose, p2: Pose):
        return math.hypot(p1.x - p2.x, p1.y - p2.y)

    def check_collision(self):
        if self.player_position is None:
            return
        for name, pose in list(self.enemies_position.items()):
            d = self.find_distance(self.player_position, pose)
          
            if d < 0.5:
                self.get_logger().info(f"Hit detected: {name} (dist={d:})")
                self.kill_enemy(name, respawn=True)
                self.score += 1
                msg = Int32()
                msg.data = self.score
                self.score_publisher.publish(msg)
                self.get_logger().info(f"Score: {self.score}")

def main(args=None):
    rclpy.init(args=args)
    node = TurtleChase()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
