import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from example_interfaces.srv import SetBool

class MyNode(Node):
    def __init__(self):
        super().__init__("motor")
        
        self.pubber = self.create_publisher(Int32, "sicaklik", 10)
        self.create_service(SetBool, "on_off", self.on_off_arandi)
        
        self.create_timer(0.5, self.timer_cb)


        self.sicaklik = 0
        self.durum = True

    def timer_cb(self):
        if self.durum:
            self.sicaklik += 1
        else:
            self.sicaklik -= 1

        msg = Int32()
        msg.data = self.sicaklik

        self.pubber.publish(msg)


    def on_off_arandi(self, req: SetBool.Request, res: SetBool.Response) -> SetBool.Response:

        self.durum = req.data
        res.success = True

        return res

def main():
    rclpy.init()

    n = MyNode()

    rclpy.spin(n)