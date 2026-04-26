import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist



class MyNode(Node):
    def __init__(self):
        super().__init__("benim_node")
        self.pubber = self.create_publisher(String, "merhaba", 10)
        self.create_timer(1.0, self.timer_cb)

    def timer_cb(self):
        msg = Twist()
        msg.linear.x = 1.0
        self.pubber.publish(msg)

    def git(self, lin=0.0, ang=0.0):
        msg = Twist()
        msg.linear.x = lin
        msg.angular.z = ang
        self.pubber.publish()


def main():
    rclpy.init()
        
    n = MyNode()

    while True:
        girdi = input("girdi girin: ")
        if girdi == "w":
            n.git(1.0, 0.0)
        elif girdi == "a":
            n.git(0.0, 1.0)
        elif girdi == "s":
            n.git(-1.0, 0.0)
        elif girdi == "d":
            n.git(0.0, -1.0)

        rclpy.spin_once(n, timeout_sec=0.5)
