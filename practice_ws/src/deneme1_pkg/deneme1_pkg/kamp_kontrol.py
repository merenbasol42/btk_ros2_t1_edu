import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class MyNode(Node):
    def __init__(self):
        super().__init__("kontrol")
        self.pubber = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
    
    def git(self, lin: float, ang: float):
        msg = Twist()
        msg.linear.x = lin
        msg.angular.z = ang

        self.pubber.publish(msg)


def main():
    rclpy.init()

    n = MyNode()

    while True:
        girdi = input(": ")
        if girdi == "w":
            n.git(1.0, 0.0)
        elif girdi == "a":
            n.git(0.0, 1.0)
        elif girdi == "s":
            n.git(-1.0, 0.0)
        elif girdi == "d":
            n.git(0.0, -1.0)
        
        rclpy.spin_once(n, timeout_sec=0.5)

        
