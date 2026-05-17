import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter

from rcl_interfaces.msg import SetParametersResult


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
        
        self.declare_parameter("lin_hiz", 4.0)
        self.lin_hiz: float = self.get_parameter("lin_hiz").value
        self.add_on_set_parameters_callback(self.on_param)

    def on_param(self, params: list[Parameter]):

        for param in params:
            if param.name == "lin_hiz":
                self.lin_hiz = param.value

        result = SetParametersResult()
        result.successful = True

        return result


    def pose_geldi(self, msg: Pose):
        hiz_msg = Twist()
        hiz_msg.linear.x = self.lin_hiz

        if msg.x > ESIK_MAX or msg.y > ESIK_MAX or msg.x < ESIK_MIN or msg.y < ESIK_MIN:
            hiz_msg.angular.z = 3.0 

        self.hiz_yayimlayicisi.publish(hiz_msg)  

def main():
    rclpy.init()
    n = MyNode()
    rclpy.spin(n)