import rclpy
import random
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.parameter_client import AsyncParameterClient
from rcl_interfaces.msg import SetParametersResult

import time
import math

from geometry_msgs.msg import Twist, Pose

from turtlesim.msg import Pose
from turtlesim.srv import Kill, Spawn, SetPen




class MyNode(Node):
    def __init__(self):
        super().__init__("avci_uygulama")

        self.kaplumbagalar: list[Spawn.Request] = []

        self.enson_spawn_zamani: float = time.time()

        self.kaplumbaga_isim_sayac = 2

        self.avci_pose: Pose = Pose()


        self.declare_parameter("lin_kp", 1.5)
        self.lin_kp: float = self.get_parameter("lin_kp").value

        self.declare_parameter("ang_kp", 2.25)
        self.ang_kp: float = self.get_parameter("ang_kp").value

        self.add_on_set_parameters_callback(self.on_param)

        self.hiz_yayimlayici = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.create_subscription(Pose, "turtle1/pose", self.pose_geldi, 10)

        self.client_kill = self.create_client(Kill, "kill")
        self.client_spawn = self.create_client(Spawn, "spawn")
        self.client_setpen = self.create_client(SetPen, "turtle1/set_pen")

        while not self.client_kill.wait_for_service(1.0):
            self.get_logger().warn("kill servisi bekleniyor")

        while not self.client_spawn.wait_for_service(1.0):
            self.get_logger().warn("spawn servisi bekleniyor")

        cli = AsyncParameterClient(self, "turtlesim")
        p_b = Parameter("background_b", Parameter.Type.INTEGER, 125)
        p_g = Parameter("background_g", Parameter.Type.INTEGER, 125)
        p_r = Parameter("background_r", Parameter.Type.INTEGER, 125)


        cli.set_parameters([p_b, p_g, p_r])

        self.create_timer(0.05, self.calis)

    def on_param(self, params: list[Parameter]) -> SetParametersResult:
        res = SetParametersResult()
        res.successful = True
        for param in params:
            if param.name == "lin_kp":
                self.lin_kp = param.value
            elif param.name == "ang_kp":
                self.ang_kp = param.value
        return res

    def calis(self):
        # print(self.kaplumbagalar)
        self.kontrol_spawn()
        self.kontrol_olum()
        self.avla()
        self.ren_degis()


    def pose_geldi(self, msg: Pose):
        self.avci_pose.x = msg.x
        self.avci_pose.y = msg.y
        self.avci_pose.theta = msg.theta


    def ren_degis(self):
        req = SetPen.Request()
        req.r = random.randint(0,255)
        req.g = random.randint(0,255)
        req.b = random.randint(0,255)
        req.width = 2

        self.client_setpen.call_async(req)


    def kontrol_spawn(self):
        if len(self.kaplumbagalar) >= 5:
            return
        
        simdi = time.time()
        if simdi - self.enson_spawn_zamani > 0.3:
            req = Spawn.Request()
            req.name = f"turtle{self.kaplumbaga_isim_sayac}"
            self.kaplumbaga_isim_sayac += 1
            
            req.x = random.random() * 10 + 2
            req.y = random.random() * 10 + 2
            req.theta = random.random() * 6.28 - 3.14

            self.client_spawn.call_async(req)
            self.kaplumbagalar.append(req)
            self.enson_spawn_zamani = simdi

    def kontrol_olum(self):
        for i in range(len(self.kaplumbagalar)):
            mesafe = self.mesafe_hesapla(i)
            if mesafe < 1.0:
                req = Kill.Request()
                req.name = self.kaplumbagalar[i].name
                self.client_kill.call_async(req)
                self.kaplumbagalar.pop(i)
                return


    def avla(self):
        if len(self.kaplumbagalar) == 0:
            return
        
        k_i = self.en_yakin_kamp_bul()
        msg = Twist()
        msg.linear.x = self.lin_kp * self.mesafe_hesapla(k_i) + 0.2
        msg.angular.z = self.ang_kp * self.aci_hesapla(k_i)
        self.hiz_yayimlayici.publish(msg)


    def mesafe_hesapla(self, k_index: int) -> float:
        k = self.kaplumbagalar[k_index]
        x_farki = k.x - self.avci_pose.x
        y_farki = k.y - self.avci_pose.y

        return math.sqrt(x_farki**2 + y_farki**2) 
    
    def en_yakin_kamp_bul(self) -> int:
        en_yakin = 100000.0
        hedef = -1

        for i in range(len(self.kaplumbagalar)):
            mesafe = self.mesafe_hesapla(i)
            if mesafe < en_yakin:
                en_yakin = mesafe
                hedef = i

        return hedef

    def aci_hesapla(self, k_index: int) -> float:
        k = self.kaplumbagalar[k_index]
        x_farki = k.x - self.avci_pose.x
        y_farki = k.y - self.avci_pose.y

        beta = math.atan2(y_farki, x_farki)

        aci = beta - self.avci_pose.theta

        if aci > 3.14:
            aci -= 2 * 3.14
        elif aci < -3.14:
            aci += 2 * 3.14

        return aci
    



def main():
    rclpy.init()
    n = MyNode()
    rclpy.spin(n)