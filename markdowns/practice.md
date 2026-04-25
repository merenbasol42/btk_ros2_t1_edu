# Pratik Alıştırmalar

## 5. Haberleşme

### Publisher

Her saniye `/chatter` topic'ine `String` mesajı yayınlayan node.

```python
# publisher.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.callback)
        self.count = 0

    def callback(self):
        msg = String()
        msg.data = f'Merhaba! Mesaj no: {self.count}'
        self.pub.publish(msg)
        self.get_logger().info(f'Yayınlandı: {msg.data}')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

```bash
python3 publisher.py
```

Çalıştırdığınızda şunu görürsünüz:
```
[INFO] [minimal_publisher]: Yayınlandı: Merhaba! Mesaj no: 0
[INFO] [minimal_publisher]: Yayınlandı: Merhaba! Mesaj no: 1
[INFO] [minimal_publisher]: Yayınlandı: Merhaba! Mesaj no: 2
```

---

### Subscriber

`/chatter` topic'ini dinleyip gelen her mesajı terminale basan node.

```python
# subscriber.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.sub = self.create_subscription(String, 'chatter', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'Alındı: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = MinimalSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

```bash
python3 subscriber.py
```

Çalıştırdığınızda şunu görürsünüz:
```
[INFO] [minimal_subscriber]: Alındı: Merhaba! Mesaj no: 0
[INFO] [minimal_subscriber]: Alındı: Merhaba! Mesaj no: 1
```

---

### Publisher ve Subscriber Birlikte

Publisher ve subscriber'ı aynı anda çalıştırmak için iki ayrı terminal açın.

**Terminal 1:**
```bash
python3 publisher.py
```

**Terminal 2:**
```bash
python3 subscriber.py
```

Terminal 2'de şunu görürsünüz:
```
[INFO] [minimal_subscriber]: Alındı: Merhaba! Mesaj no: 3
[INFO] [minimal_subscriber]: Alındı: Merhaba! Mesaj no: 4
[INFO] [minimal_subscriber]: Alındı: Merhaba! Mesaj no: 5
```

---

### Servis Sunucusu

`/add_two_ints` servisini açan, iki sayıyı toplayıp döndüren sunucu.

```python
# add_server.py
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__('add_two_ints_server')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.callback)

    def callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'{request.a} + {request.b} = {response.sum}')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

```bash
python3 add_server.py
```

İstemci bağlanınca şunu görürsünüz:
```
[INFO] [add_two_ints_server]: 3 + 7 = 10
```

---

### Servis İstemcisi

`/add_two_ints` servisine istek gönderip sonucu ekrana basan istemci.

```python
# add_client.py
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis bekleniyor...')

    def send(self, a, b):
        req = AddTwoInts.Request()
        req.a = a
        req.b = b
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result().sum


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    result = node.send(3, 7)
    node.get_logger().info(f'Sonuç: {result}')
    node.destroy_node()
    rclpy.shutdown()
```

**Terminal 1'de sunucuyu başlatın, Terminal 2'de istemciyi çalıştırın:**
```bash
python3 add_client.py
```

Terminal 2'de şunu görürsünüz:
```
[INFO] [add_two_ints_client]: Sonuç: 10
```

---

### Aksiyon Sunucusu

Verilen `order` kadar Fibonacci sayısını hesaplayıp her adımda geri bildirim gönderen sunucu.

```python
# fibonacci_server.py
import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from example_interfaces.action import Fibonacci


class FibonacciServer(Node):
    def __init__(self):
        super().__init__('fibonacci_server')
        self._server = ActionServer(self, Fibonacci, 'fibonacci', self.execute)

    def execute(self, goal_handle):
        sequence = [0, 1]
        feedback = Fibonacci.Feedback()

        for _ in range(1, goal_handle.request.order):
            sequence.append(sequence[-1] + sequence[-2])
            feedback.partial_sequence = sequence
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f'Geri bildirim: {sequence}')
            time.sleep(0.5)

        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = sequence
        return result


def main(args=None):
    rclpy.init(args=args)
    node = FibonacciServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

```bash
python3 fibonacci_server.py
```

İstemci bağlanınca şunu görürsünüz:
```
[INFO] [fibonacci_server]: Geri bildirim: [0, 1, 1]
[INFO] [fibonacci_server]: Geri bildirim: [0, 1, 1, 2]
[INFO] [fibonacci_server]: Geri bildirim: [0, 1, 1, 2, 3]
```

---

### Aksiyon İstemcisi

Fibonacci sunucusuna `order=5` hedefi gönderir ve gelen geri bildirimleri ekrana basar.

```python
# fibonacci_client.py
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from example_interfaces.action import Fibonacci


class FibonacciClient(Node):
    def __init__(self):
        super().__init__('fibonacci_client')
        self._client = ActionClient(self, Fibonacci, 'fibonacci')

    def send_goal(self, order):
        self._client.wait_for_server()
        goal = Fibonacci.Goal()
        goal.order = order
        future = self._client.send_goal_async(goal, feedback_callback=self.feedback_cb)
        rclpy.spin_until_future_complete(self, future)
        goal_handle = future.result()
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        self.get_logger().info(f'Sonuç: {list(result_future.result().result.sequence)}')

    def feedback_cb(self, feedback):
        self.get_logger().info(f'Geri bildirim: {list(feedback.feedback.partial_sequence)}')


def main(args=None):
    rclpy.init(args=args)
    node = FibonacciClient()
    node.send_goal(5)
    node.destroy_node()
    rclpy.shutdown()
```

**Terminal 1'de sunucuyu başlatın, Terminal 2'de istemciyi çalıştırın:**
```bash
python3 fibonacci_client.py
```

Terminal 2'de şunu görürsünüz:
```
[INFO] [fibonacci_client]: Geri bildirim: [0, 1, 1]
[INFO] [fibonacci_client]: Geri bildirim: [0, 1, 1, 2]
[INFO] [fibonacci_client]: Geri bildirim: [0, 1, 1, 2, 3]
[INFO] [fibonacci_client]: Geri bildirim: [0, 1, 1, 2, 3, 5]
[INFO] [fibonacci_client]: Sonuç: [0, 1, 1, 2, 3, 5]
```

---

### Özel Mesaj Tanımı: SensorReading.msg

Sıcaklık ve nem taşıyan özel bir mesaj tanımı oluşturup publisher/subscriber ile kullanma.

**Adım 1 — Arayüz paketi oluşturun:**
```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_cmake sensor_interfaces
mkdir sensor_interfaces/msg
```

**Adım 2 — Mesaj dosyasını yazın (`sensor_interfaces/msg/SensorReading.msg`):**
```
float32 temperature
float32 humidity
string unit
```

**Adım 3 — `sensor_interfaces/CMakeLists.txt`'i güncelleyin (`find_package(ament_cmake REQUIRED)` satırından sonra ekleyin):**
```cmake
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/SensorReading.msg"
)
```

**Adım 4 — `sensor_interfaces/package.xml`'e ekleyin (`<buildtool_depend>ament_cmake</buildtool_depend>` satırından sonra):**
```xml
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```

**Adım 5 — Derleyin ve kaynak edin:**
```bash
cd ~/ros2_ws
colcon build --packages-select sensor_interfaces
source install/setup.bash
```

**Adım 6 — Publisher (`sensor_publisher.py`):**
```python
import rclpy
from rclpy.node import Node
from sensor_interfaces.msg import SensorReading


class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.pub = self.create_publisher(SensorReading, 'sensor_data', 10)
        self.timer = self.create_timer(1.0, self.callback)

    def callback(self):
        msg = SensorReading()
        msg.temperature = 23.5
        msg.humidity = 60.0
        msg.unit = 'celsius'
        self.pub.publish(msg)
        self.get_logger().info(f'Yayınlandı: {msg.temperature}°C, {msg.humidity}%')


def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

**Adım 7 — Subscriber (`sensor_subscriber.py`):**
```python
import rclpy
from rclpy.node import Node
from sensor_interfaces.msg import SensorReading


class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.sub = self.create_subscription(SensorReading, 'sensor_data', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(
            f'Alındı — Sıcaklık: {msg.temperature}{msg.unit}, Nem: {msg.humidity}%'
        )


def main(args=None):
    rclpy.init(args=args)
    node = SensorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

Subscriber çalıştırıldığında şunu görürsünüz:
```
[INFO] [sensor_subscriber]: Alındı — Sıcaklık: 23.5celsius, Nem: 60.0%
```

---

## 6. Paketler ve Çalışma Alanları

### Sıfırdan workspace → paket → publisher → çalıştır

**1 — Workspace oluşturun:**
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

**2 — Paket oluşturun:**
```bash
cd src
ros2 pkg create --build-type ament_python demo_pkg
```

Beklenen çıktı:
```
going to create a new package
package name: demo_pkg
...
creating ./demo_pkg/setup.py
creating ./demo_pkg/demo_pkg/__init__.py
```

**3 — Publisher node'unu yazın (`demo_pkg/demo_pkg/talker.py`):**
```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.callback)
        self.count = 0

    def callback(self):
        msg = String()
        msg.data = f'Selam {self.count}'
        self.pub.publish(msg)
        self.get_logger().info(msg.data)
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

**4 — `demo_pkg/setup.py`'deki `entry_points`'e talker'ı ekleyin:**
```python
entry_points={
    'console_scripts': [
        'talker = demo_pkg.talker:main',
    ],
},
```

**5 — `demo_pkg/package.xml`'e `std_msgs` bağımlılığını ekleyin:**
```xml
<exec_depend>rclpy</exec_depend>
<exec_depend>std_msgs</exec_depend>
```

**6 — Derleyin, kaynak edin, çalıştırın:**
```bash
cd ~/ros2_ws
colcon build --packages-select demo_pkg
source install/setup.bash
ros2 run demo_pkg talker
```

Çalıştırdığınızda şunu görürsünüz:
```
Starting >>> demo_pkg
Finished <<< demo_pkg [1.2s]

Summary: 1 package finished [1.4s]

[INFO] [talker]: Selam 0
[INFO] [talker]: Selam 1
[INFO] [talker]: Selam 2
```

---

## 7. Parametreler

### Parametre tanımlama, okuma ve YAML ile yükleme

Node başladığında YAML dosyasından `hiz_siniri` ve `robot_adi` parametrelerini yükleyen node.

**`demo_pkg/demo_pkg/param_node.py`:**
```python
import rclpy
from rclpy.node import Node


class ParamNode(Node):
    def __init__(self):
        super().__init__('param_node')
        self.declare_parameter('hiz_siniri', 1.0)
        self.declare_parameter('robot_adi', 'robot_1')
        self.timer = self.create_timer(2.0, self.callback)

    def callback(self):
        hiz = self.get_parameter('hiz_siniri').get_parameter_value().double_value
        isim = self.get_parameter('robot_adi').get_parameter_value().string_value
        self.get_logger().info(f'{isim} — hız sınırı: {hiz}')


def main(args=None):
    rclpy.init(args=args)
    node = ParamNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

**`demo_pkg/config/robot.yaml`:**
```yaml
param_node:
  ros__parameters:
    hiz_siniri: 2.5
    robot_adi: "atlas"
```

**`demo_pkg/launch/param_launch.py`:**
```python
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('demo_pkg'), 'config', 'robot.yaml'
    )
    return LaunchDescription([
        Node(
            package='demo_pkg',
            executable='param_node',
            parameters=[config],
            output='screen',
        )
    ])
```

`setup.py`'ye config ve launch dizinlerini kayıt edin (`data_files` listesine ekleyin):
```python
import os
from glob import glob

data_files=[
    ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
],
```

```bash
colcon build --packages-select demo_pkg
source install/setup.bash
ros2 launch demo_pkg param_launch.py
```

Çalıştırdığınızda şunu görürsünüz:
```
[INFO] [param_node]: atlas — hız sınırı: 2.5
[INFO] [param_node]: atlas — hız sınırı: 2.5
```

---

### Çalışırken parametre güncelleme ve doğrulama

Node çalışırken `hiz_siniri` değiştiğinde callback tetiklenir; negatif değerler reddedilir.

**`demo_pkg/demo_pkg/validated_param_node.py`:**
```python
import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult


class ValidatedParamNode(Node):
    def __init__(self):
        super().__init__('validated_param_node')
        self.declare_parameter('hiz_siniri', 1.0)
        self.add_on_set_parameters_callback(self.on_param_change)
        self.timer = self.create_timer(2.0, self.callback)

    def on_param_change(self, params):
        for p in params:
            if p.name == 'hiz_siniri' and p.value < 0.0:
                return SetParametersResult(successful=False, reason='Hız negatif olamaz')
        return SetParametersResult(successful=True)

    def callback(self):
        hiz = self.get_parameter('hiz_siniri').get_parameter_value().double_value
        self.get_logger().info(f'Mevcut hız sınırı: {hiz}')


def main(args=None):
    rclpy.init(args=args)
    node = ValidatedParamNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

Node çalışırken **başka bir terminalde** parametreyi güncelleyin:
```bash
ros2 param set /validated_param_node hiz_siniri 3.0
```
```
Set parameter successful
```

Negatif değer gönderin:
```bash
ros2 param set /validated_param_node hiz_siniri -1.0
```
```
Setting parameter failed: Hız negatif olamaz
```

---

### `ros2 param set` ile dışarıdan değer gönderme

`validated_param_node` çalışırken tüm parametre işlemlerini terminalden yapın.

**Parametreleri listele:**
```bash
ros2 param list /validated_param_node
```
```
  hiz_siniri
  use_sim_time
```

**Değeri oku:**
```bash
ros2 param get /validated_param_node hiz_siniri
```
```
Double value is: 1.0
```

**Değeri güncelle:**
```bash
ros2 param set /validated_param_node hiz_siniri 2.0
```
```
Set parameter successful
```

**Tüm parametreleri YAML olarak dışa aktar:**
```bash
ros2 param dump /validated_param_node
```
```
/validated_param_node:
  ros__parameters:
    hiz_siniri: 2.0
    use_sim_time: false
```

---

## 8. Gözlem Araçları

### rosbag2: kayıt al, publisher'ı kapat, bag'i oynat

Publisher çalışırken mesajları kaydedin. Publisher'ı kapattıktan sonra bag'i oynatın; subscriber hâlâ mesaj almaya devam eder.

**Terminal 1 — Publisher'ı başlatın:**
```bash
python3 publisher.py
```

**Terminal 2 — Tüm topic'leri kaydedin:**
```bash
ros2 bag record -a -o sensor_bag
```
```
[INFO] [rosbag2_recorder]: Listening for topics...
[INFO] [rosbag2_recorder]: Subscribed to topic '/chatter'
[INFO] [rosbag2_recorder]: Recording...
```

**Terminal 3 — Subscriber'ı başlatın (mesaj aldığını doğrulayın):**
```bash
python3 subscriber.py
```

30 saniye sonra Terminal 1'de `Ctrl+C` ile publisher'ı, Terminal 2'de kaydı durdurun. Terminal 3'teki subscriber'ı çalışır bırakın.

**Bag'i oynatın:**
```bash
ros2 bag play sensor_bag/
```

Terminal 3'te kaydedilen mesajların tekrar geldiğini görürsünüz:
```
[INFO] [minimal_subscriber]: Alındı: Merhaba! Mesaj no: 0
[INFO] [minimal_subscriber]: Alındı: Merhaba! Mesaj no: 1
```

**Kayıt hakkında bilgi alın:**
```bash
ros2 bag info sensor_bag/
```
```
Files:             sensor_bag_0.db3
Bag size:          48.6 KiB
Duration:          30.1s
Messages:          30
Topic information: Topic: /chatter | Type: std_msgs/msg/String | Count: 30
```

---

### rqt_graph: iki node çalışırken bağlantıyı görselleştir

**Terminal 1:**
```bash
python3 publisher.py
```

**Terminal 2:**
```bash
python3 subscriber.py
```

**Terminal 3:**
```bash
ros2 run rqt_graph rqt_graph
```

Açılan pencerede şunu görürsünüz:

```
[/minimal_publisher] --(/chatter)--> [/minimal_subscriber]
```

Sol üstteki açılır menüden **"Nodes/Topics (all)"** seçin; tüm topic'ler ve bağlantılar görünür hale gelir.

---

### ros2 topic hz ve echo ile canlı izleme

**Terminal 1 — Publisher:**
```bash
python3 publisher.py
```

**Terminal 2 — Gelen mesajları ekrana bas:**
```bash
ros2 topic echo /chatter
```
```
data: 'Merhaba! Mesaj no: 4'
---
data: 'Merhaba! Mesaj no: 5'
---
```

**Terminal 3 — Yayın frekansını ölç:**
```bash
ros2 topic hz /chatter
```
```
average rate: 1.000
	min: 1.000s max: 1.000s std dev: 0.00003s window: 10
```

---

## 9. Launch Sistemi

### İki node'u tek launch dosyasıyla başlatma

Publisher (`talker`) ve subscriber (`listener`) node'larını tek komutla başlatan launch dosyası. `listener` node'unu da `demo_pkg` içinde `setup.py`'ye kaydettiğinizi varsayar.

**`demo_pkg/launch/talker_listener.launch.py`:**
```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_pkg',
            executable='talker',
            output='screen',
        ),
        Node(
            package='demo_pkg',
            executable='listener',
            output='screen',
        ),
    ])
```

```bash
ros2 launch demo_pkg talker_listener.launch.py
```

Çalıştırdığınızda şunu görürsünüz:
```
[talker-1] [INFO] [talker]: Selam 0
[listener-2] [INFO] [listener]: Alındı: Selam 0
[talker-1] [INFO] [talker]: Selam 1
[listener-2] [INFO] [listener]: Alındı: Selam 1
```

---

### `use_sim_time` argümanı geçme

Çalışma zamanında `true` veya `false` geçilebilen `use_sim_time` argümanı içeren launch dosyası.

**`demo_pkg/launch/sim_launch.py`:**
```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Simülasyon saatini etkinleştir',
    )

    node = Node(
        package='demo_pkg',
        executable='talker',
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
        output='screen',
    )

    return LaunchDescription([use_sim_time_arg, node])
```

**Varsayılan değerle başlat:**
```bash
ros2 launch demo_pkg sim_launch.py
```

**Simülasyon saatiyle başlat:**
```bash
ros2 launch demo_pkg sim_launch.py use_sim_time:=true
```

**Kabul edilen argümanları göster:**
```bash
ros2 launch demo_pkg sim_launch.py --show-args
```
```
Arguments (pass arguments as '<name>:=<value>'):

    'use_sim_time':
        Simülasyon saatini etkinleştir
        (default: 'false')
```

---

### Namespace ile aynı node'dan iki örnek (robot1, robot2)

Aynı `talker` node'undan iki bağımsız örnek, farklı namespace'ler altında çalışır; topic isimleri çakışmaz.

**`demo_pkg/launch/multi_robot.launch.py`:**
```python
from launch import LaunchDescription
from launch.actions import GroupAction
from launch_ros.actions import Node, PushRosNamespace


def generate_launch_description():
    robot1 = GroupAction([
        PushRosNamespace('robot1'),
        Node(package='demo_pkg', executable='talker', output='screen'),
    ])

    robot2 = GroupAction([
        PushRosNamespace('robot2'),
        Node(package='demo_pkg', executable='talker', output='screen'),
    ])

    return LaunchDescription([robot1, robot2])
```

```bash
ros2 launch demo_pkg multi_robot.launch.py
```

Çalıştırdığınızda şunu görürsünüz:
```
[talker-1] [INFO] [robot1.talker]: Selam 0
[talker-2] [INFO] [robot2.talker]: Selam 0
[talker-1] [INFO] [robot1.talker]: Selam 1
[talker-2] [INFO] [robot2.talker]: Selam 1
```

Topic'lerin ayrı namespace altında oluştuğunu doğrulayın:
```bash
ros2 topic list
```
```
/robot1/chatter
/robot2/chatter
```

---

### IfCondition ile rviz2'yi isteğe bağlı açma

`launch_rviz:=true` geçildiğinde rviz2'yi de başlatan, geçilmediğinde yalnızca talker'ı çalıştıran launch dosyası.

**`demo_pkg/launch/conditional_launch.py`:**
```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    launch_rviz_arg = DeclareLaunchArgument(
        'launch_rviz',
        default_value='false',
        description="true ise rviz2'yi başlat",
    )

    talker = Node(
        package='demo_pkg',
        executable='talker',
        output='screen',
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        condition=IfCondition(LaunchConfiguration('launch_rviz')),
    )

    return LaunchDescription([launch_rviz_arg, talker, rviz])
```

**Sadece talker ile başlat (varsayılan):**
```bash
ros2 launch demo_pkg conditional_launch.py
```

**Talker + rviz2 ile başlat:**
```bash
ros2 launch demo_pkg conditional_launch.py launch_rviz:=true
```
```
[talker-1] [INFO] [talker]: Selam 0
[rviz2-2] [INFO] [rviz2]: Loading...
```
