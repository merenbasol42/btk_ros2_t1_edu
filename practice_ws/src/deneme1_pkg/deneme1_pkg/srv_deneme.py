# import rclpy
# from rclpy.node import Node

# from example_interfaces.srv import SetBool



# class MyNode(Node):
#     def __init__(self):
#         super().__init__("benim_node")
#         self.create_service(AddTwoInts, "carpim", self.srv_arandi)
#         self.durum = True

#     def srv_arandi(self, istek: SetBool.Request, yanit: SetBool.Response) -> SetBool.Response:
#         if istek.data:
#             self.durum = True
#         else:
#             self

#         return yanit
    

def main():
    pass
    # rclpy.init()

    # n = MyNode()
    # rclpy.spin(n)