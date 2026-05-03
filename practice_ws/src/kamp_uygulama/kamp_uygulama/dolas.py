import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

KENAR_MIN: float = 0.0
KENAR_MAX: float = 11.0

ESIK_MIN: float = 2.0
ESIK_MAX: float = 9.0


class MyNode(Node):
    def __init__(self):
        super().__init__("dolas")
        self.hiz_yayimlayicisi = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.create_subscription(Pose, "turtle1/pose", self.pose_geldi, 10)
        

    def pose_geldi(self, msg: Pose):
        hiz_msg = Twist()
        hiz_msg.linear.x = 2.5
        hata = 0.0

        if msg.x > ESIK_MAX:
            hata = ESIK_MAX - msg.x 
        elif msg.x < ESIK_MIN:
            hata = msg.x - ESIK_MIN
        if msg.y > ESIK_MAX:
            hata = ESIK_MAX - msg.y  
        elif msg.y < ESIK_MIN:
            hata = msg.y - ESIK_MIN
          
        hiz_msg.angular.z = hata * 3.0 

        self.hiz_yayimlayicisi.publish(hiz_msg)  

def main():
    rclpy.init()
    n = MyNode()
    rclpy.spin(n)