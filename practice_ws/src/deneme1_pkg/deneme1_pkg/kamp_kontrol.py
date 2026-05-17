import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter

from rcl_interfaces.msg import SetParametersResult, ParameterDescriptor, FloatingPointRange

from geometry_msgs.msg import Twist

class MyNode(Node):
    def __init__(self):
        super().__init__("kontrol")
        self.pubber = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        desc = ParameterDescriptor()
        desc.description = "kapblumanaga kosnol cartcurt"
        desc.floating_point_range = [
            FloatingPointRange(
                from_value=0.0,
                to_value=5.0,
            )
        ]


        self.declare_parameter("lineer_hiz", 3.0, descriptor=desc)
        self.lineer_hiz: float = self.get_parameter("lineer_hiz").value

        self.declare_parameter("acisal_hiz", 3.0)
        self.acisal_hiz: float = self.get_parameter("acisal_hiz").value

        self.add_on_set_parameters_callback(self.on_param)

    def on_param(self, params: list[Parameter]) -> SetParametersResult:
        result = SetParametersResult()
        result.successful = True

        for param in params:
            if param.name == "lineer_hiz":
                self.lineer_hiz: float = param.value  
            elif param.name == "acisal_hiz":
                self.acisal_hiz: float = param.value  

        return result

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
            n.git(n.lineer_hiz, 0.0)
        elif girdi == "a":
            n.git(0.0, n.acisal_hiz)
        elif girdi == "s":
            n.git(-n.lineer_hiz, 0.0)
        elif girdi == "d":
            n.git(0.0, -n.acisal_hiz)
        
        rclpy.spin_once(n, timeout_sec=0.5)

        
