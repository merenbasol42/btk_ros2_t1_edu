# İçindekiler

- [1. Giriş](#1-giriş)
- [2. Teori](#2-teori)
  - [2.1 Topic](#21-topic)
  - [2.2 Service](#22-service)
  - [2.3 Action Service](#23-action-service)
  - [2.4 Özel Mesaj Arayüzleri](#24-özel-mesaj-arayüzleri)
- [3. Kullanım](#3-kullanım)
  - [3.1 API (Python)](#31-api-python)
    - [3.1.1 Topic](#311-topic)
    - [3.1.2 Service](#312-service)
    - [3.1.3 Action Service](#313-action-service)
    - [3.1.4 Özel Mesaj Arayüzleri](#314-özel-mesaj-arayüzleri)
  - [3.2 CLI](#32-cli)
  - [3.3 Genel Tavsiye](#33-genel-tavsiye)

---

# 1. Giriş

Bu dosya, `theory.md`'de tanıdığınız düğüm ve çizge kavramlarının bir adım ötesine taşır: ROS2 düğümlerinin birbirleriyle nasıl konuştuğunu ele alır. Yani haberleşme altyapısını hem teorik hem de uygulama düzeyinde inceliyoruz.

Bu dosyayı okuduğunuzda şunları öğrenmiş olacaksınız:

- ROS2'nin üç temel iletişim türünün ne işe yaradığını ve hangisinin ne zaman tercih edileceğini
- Bu iletişim türlerini Python'da nasıl yazacağınızı — çalışan, açıklamalı örneklerle
- `ros2` CLI araçlarını kullanarak düğümlerinizi terminal üzerinden nasıl izleyip test edeceğinizi

Hazırsanız başlayalım.

---

# 2. Teori

ROS'ta iletişim **kanallar** üzerinden yapılır. Bu kanallar 3 tiptir: **topic**, **service** ve **action service**.

Her kanalın uyması gereken iki temel kural vardır:

1. Her kanalın benzersiz bir ismi olmalı
2. Her kanalın bir mesaj tipi olmalı

Bu iki kural, tüm iletişim türleri için geçerlidir.

## 2.1 Topic

Topic kanalında iki tür iletişimci vardır: **yayımcı (publisher)** ve **abone (subscriber)**.

<div align="center">
  <img src="./ros-gif/topic.gif">
</div>

Yayımcı kanala veri yollar, abone ise o kanalı dinleyip gelen mesajlardan haberdar olur. Abone olurken bir "callback" fonksiyonu verirsiniz; ROS da mesaj geldiğinde bu fonksiyonu çağırarak size veriyi teslim eder.

> **Gerçek hayat örneği:** Radyo. Bir frekansı ayarlarsınız — diyelim 98.1 — ve artık o frekanstaki yayınları dinlersiniz. Bir frekansa birden fazla dinleyici olabileceği gibi, birden fazla yayıncı da olabilir. Topic kanalı da tıpkı bunun gibidir.

## 2.2 Service

Servisler klasik **server–client** mantığıyla çalışır. Sunucu bir servis kanalı açar ve bir callback fonksiyon tanımlar. İstemci, bu servise bir istek gönderir ve karşılığında mutlaka bir yanıt alır.

<div align="center">
  <img src="./ros-gif/service.gif">
</div>

Servisler, "mesaj gönder, cevap al" tarzı iletişimlerde kullanılır. Topic ile bu tür bir yanıt garantisini elde edemezsiniz, ama service size bunu sağlar.

> **Gerçek hayat örneği:** Restoran siparişi.
> 1. Müşteri (Client) garsona sipariş verir: *"Bir pizza istiyorum."*
> 2. Garson (Server) isteği alır, mutfağa iletir ve sonucu bekler.
> 3. Pizza hazır olduğunda garson müşteriye teslim eder: *"Buyurun, pizzanız hazır!"*
> 4. Müşteri (Client) yanıtı aldıktan sonra işlem tamamlanır.

## 2.3 Action Service

Aksiyon servisleri, iki servis + bir topic birleşimi gibidir. Uzun süren işlemlerde, ara ara bilgi almak veya süreci takip etmek istediğimizde kullanılır.

<div align="center">
  <img src="./ros-gif/action.gif">
</div>

Örneğin, robotunuza "şu konuma git ve dengede kal" diyorsunuz. Robot dengede kalmaya çalışırken siz de "şu anda hız sınırını aşıyor mu, ne kadar kaldı" gibi bilgileri almak istiyorsunuz. İşte burada action servisleri devreye giriyor.

> **Gerçek hayat örneği:** Robota "şu raftaki kutuyu al ve bana getir" komutu veriyorsunuz.
> 1. Komutu gönderiyorsunuz — robot hedefi kabul ediyor
> 2. Robot ilerlerken size düzenli konum bildirimi gönderiyor: *"Rafa 2 metre kaldı… 1 metre kaldı… kutuyu aldım…"*
> 3. Robot kutunun önüne ulaştığında *"görev tamamlandı"* yanıtını döndürüyor

Yani hem süreç takibi yapabiliyor, hem de sonunda sonucu alabiliyorsunuz.

## 2.4 Özel Mesaj Arayüzleri

İki düğümün birbiriyle konuşabilmesi için aynı "dili" konuşmaları gerekir — yani aynı mesaj formatını kullanmaları. Buna **mesaj arayüzü** diyoruz.

ROS2, sık kullanılan durumlar için hazır arayüzler sunar: `std_msgs`, `geometry_msgs`, `sensor_msgs` gibi paketlerde onlarca standart format bulunur. Bunlar bir nevi hazır kelime dağarcığı gibidir — evrensel, herkesin tanıdığı, başka paketlerle uyumlu. Mümkün olduğunda bu standartları tercih etmek hem geliştirmeyi hızlandırır hem de kodunuzu başkalarıyla paylaşmayı kolaylaştırır.

Ama bazı durumlarda bu hazır seçenekler yetmez. Robotunuzdan özel sensör verisi, fabrikaya özgü makine durumu veya projenize özel bir komut yapısı iletmeniz gerekiyorsa kendi arayüzünüzü tanımlarsınız. `.msg`, `.srv` ve `.action` dosyaları bunun için vardır — standart dağarcığa uymayan, size özel bir jargon yaratmış olursunuz.

> **Gerçek hayat örneği:** Uluslararası kargo formu. Herkesin doldurduğu standart alanlar vardır: alıcı adı, adres, ağırlık. Ama ilaç lojistiği yapan bir firma bu forma "soğuk zincir gereksinimi" ve "sıcaklık aralığı" gibi kendi alanlarını ekler. Standart form temel ihtiyacı karşılar; özel alanlar ise sektörün ihtiyacına göre şekillenir.

---

# 3. Kullanım

Teoride üç iletişim türünü ve mesaj arayüzlerini gördünüz. Bu bölümde bunları gerçekten nasıl yazacağınızı ve çalıştıracağınızı öğreneceğiz. İki açıdan ele alacağız: Python API'si ile kendi düğümlerinizi nasıl yazarsınız, ve `ros2` CLI araçlarıyla çalışan düğümleri terminal üzerinden nasıl gözlemler ve test edersiniz.

## 3.1 API (Python)

Her örnek kopyalayıp doğrudan çalıştırabileceğiniz tam bir node içeriyor. Kodun ne yaptığı satır satır açıklanmış.

### 3.1.1 Topic

#### Publisher

```python
publisher = node.create_publisher(msg_type, topic, qos_profile)
```

| Parametre | Açıklama |
|-----------|----------|
| `msg_type` | Kanaldaki mesajın Python sınıfı — örn. `std_msgs.msg.String` |
| `topic` | Kanalın adı — örn. `'/chatter'` |
| `qos_profile` | Kuyruk boyutu (int) veya tam QoS nesnesi; `10` çoğu durumda yeterlidir |

Dönen `publisher` nesnesi üzerinden mesaj yayımlanır:

```python
msg = String()
msg.data = 'merhaba'
publisher.publish(msg)
```

`publish()` çağrısı bloklayıcı değildir; mesajı ROS'un iç kuyruğuna bırakır ve hemen geri döner.

---

#### Subscriber

```python
subscription = node.create_subscription(msg_type, topic, callback, qos_profile)
```

`callback` imzası sabit: `def callback(msg)` — `msg`, `msg_type` türünden bir nesnedir. Her gelen mesajda ROS bu fonksiyonu otomatik çağırır; manuel tetikleme gerekmez.

Subscription nesnesi düşürülürse (garbage collect) abone kayıt silinir, bu yüzden genellikle `self.sub = ...` şeklinde saklanır.

---

#### Timer (topic ile birlikte sık kullanılır)

```python
timer = node.create_timer(timer_period_sec, callback)
```

Belirli aralıklarla veri yayımlamak için kullanılır. `callback` parametresiz bir fonksiyondur; `timer_period_sec` saniye cinsinden float alır.

### 3.1.2 Service

#### Server

```python
service = node.create_service(srv_type, srv_name, callback)
```

`callback` imzası: `def callback(request, response) -> response`

- `request`: istemcinin gönderdiği veriyi taşır (`srv_type.Request` türünde)
- `response`: doldurulup döndürülecek yanıt nesnesi (`srv_type.Response` türünde)

Callback, `response` nesnesini doldurmalı ve mutlaka döndürmelidir. Döndürülmezse istemci sonsuza kadar bekler.

```python
def add_callback(self, request, response):
    response.sum = request.a + request.b
    return response
```

---

#### Client

```python
client = node.create_client(srv_type, srv_name)
```

Servis hazır olmadan istek göndermek hata verir; bağlantıyı şu şekilde bekleyebilirsiniz:

```python
client.wait_for_service(timeout_sec=1.0)  # bool döner
```

İstek göndermek:

```python
request = AddTwoInts.Request()
request.a = 3
request.b = 7

future = client.call_async(request)
```

`call_async()` hemen bir `Future` nesnesi döner; sonuç hazır olduğunda içini okuyabilirsiniz:

```python
rclpy.spin_until_future_complete(node, future)
result = future.result()  # srv_type.Response türünde
```

`call_async` + `spin_until_future_complete` ikilisi en sık kullanılan senkron-görünümlü çağrı kalıbıdır; asıl işlem arka planda asenkron çalışır.

### 3.1.3 Action Service

#### ActionServer

```python
from rclpy.action import ActionServer

action_server = ActionServer(
    node,
    action_type,
    action_name,
    execute_callback
)
```

`execute_callback` imzası: `def execute_callback(goal_handle) -> Result`

`goal_handle` üzerinden üç işlem yapılır:

```python
goal_handle.request          # istemcinin gönderdiği goal verisi
goal_handle.publish_feedback(feedback_msg)  # ara ilerleme bildirimi
goal_handle.succeed()        # işlemi başarılı olarak bitir
# alternatifler: goal_handle.abort() veya goal_handle.canceled()
```

Callback, `action_type.Result()` türünde bir nesne döndürmelidir.

---

#### ActionClient

```python
from rclpy.action import ActionClient

action_client = ActionClient(node, action_type, action_name)
action_client.wait_for_server()
```

Goal göndermek:

```python
goal_msg = Fibonacci.Goal()
goal_msg.order = 10

future = action_client.send_goal_async(
    goal_msg,
    feedback_callback=feedback_cb   # opsiyonel; her feedback'te tetiklenir
)
```

`send_goal_async()` önce bir `goal_handle` future'ı döner (sunucunun kabul/red kararı). Kabul edildikten sonra result için ayrıca beklenilir:

```python
def goal_response_callback(self, future):
    goal_handle = future.result()
    result_future = goal_handle.get_result_async()
    result_future.add_done_callback(self.result_callback)
```

`feedback_callback` imzası: `def feedback_cb(feedback_msg)` — `feedback_msg.feedback` içinde sunucunun gönderdiği ara veri bulunur.

### 3.1.4 Özel Mesaj Arayüzleri

Kendi mesaj arayüzünüzü tanımlamak üç adımlı bir süreçtir: arayüz dosyalarını yazmak, paketi yapılandırmak ve Python'dan import etmek.

#### Klasör yapısı

Arayüz tanımları ayrı bir pakette tutulur (isimlendirme geleneği: `<proje>_interfaces`):

```
my_interfaces/
├── msg/
│   └── Sensor.msg
├── srv/
│   └── ComputeArea.srv
├── action/
│   └── Navigate.action
├── CMakeLists.txt
└── package.xml
```

#### Arayüz dosyaları

**`.msg`** — yalnızca alan tanımı içerir:

```
# msg/Sensor.msg
float32 temperature
float32 humidity
string unit
```

**`.srv`** — istek ve yanıt bölümleri `---` ile ayrılır:

```
# srv/ComputeArea.srv
float32 width
float32 height
---
float32 area
```

**`.action`** — goal, result ve feedback bölümleri `---` ile ayrılır:

```
# action/Navigate.action
geometry_msgs/Point target
---
bool success
string message
---
float32 distance_remaining
```

#### `CMakeLists.txt`

```cmake
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)   # başka paket mesajı kullanıyorsanız

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Sensor.msg"
  "srv/ComputeArea.srv"
  "action/Navigate.action"
  DEPENDENCIES geometry_msgs           # dışarıdan tip kullanıyorsanız ekleyin
)
```

#### `package.xml`

```xml
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>

<!-- başka paket tiplerini kullanıyorsanız -->
<depend>geometry_msgs</depend>
```

Paketi derledikten sonra (`colcon build`) arayüzler Python'dan kullanılabilir hale gelir:

```python
from my_interfaces.msg import Sensor
from my_interfaces.srv import ComputeArea
from my_interfaces.action import Navigate
```

#### Kullanım örneği

```python
# Publisher tarafında özel mesaj tipi
sensor_msg = Sensor()
sensor_msg.temperature = 23.5
sensor_msg.humidity = 60.0
sensor_msg.unit = 'celsius'
publisher.publish(sensor_msg)

# Service server tarafında özel srv tipi
def compute_callback(self, request, response):
    response.area = request.width * request.height
    return response
```

> **Not:** Arayüz paketi ile onu kullanan düğüm paketi genellikle ayrı tutulur. Böylece arayüz değişmeden düğüm kodu güncellenebilir ve farklı paketler aynı arayüzü bağımsız olarak kullanabilir.

---

## 3.2 CLI

Terminal üzerinden çalışan düğümleri incelemek ve test etmek için `ros2` komutlarını kullanırsınız.

### `ros2 topic`

```bash
# Aktif topic'leri listele
ros2 topic list

# Örnek çıktı:
# /chatter
# /parameter_events
# /rosout

# Bir topic'e gelen mesajları canlı izle
ros2 topic echo /chatter

# Örnek çıktı:
# data: 'Merhaba, dünya! Mesaj no: 5'
# ---

# Topic'e manuel mesaj yayımla (test için kullanışlı)
ros2 topic pub /chatter std_msgs/msg/String "data: 'test mesajı'"
```

### `ros2 service`

```bash
# Aktif servisleri listele
ros2 service list

# Örnek çıktı:
# /add_two_ints
# /minimal_publisher/describe_parameters

# Servisi terminal üzerinden çağır
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 4, b: 6}"

# Örnek çıktı:
# response:
#   sum: 10
```

### `ros2 action`

```bash
# Aktif action'ları listele
ros2 action list

# Örnek çıktı:
# /fibonacci

# Action'a goal gönder
ros2 action send_goal /fibonacci example_interfaces/action/Fibonacci "{order: 5}" --feedback

# Örnek çıktı:
# Feedback:
#   partial_sequence: [0, 1, 1, 2]
# ...
# Result:
#   sequence: [0, 1, 1, 2, 3]
```

### `ros2 interface`

Arayüzleri incelemek ve hangi alanların bulunduğunu öğrenmek için:

```bash
# Yüklü tüm arayüzleri listele (msg / srv / action)
ros2 interface list

# Belirli bir türü filtrele
ros2 interface list --only-msgs
ros2 interface list --only-srvs
ros2 interface list --only-actions

# Bir arayüzün alan tanımlarını göster
ros2 interface show std_msgs/msg/String
# Çıktı:
# string data

ros2 interface show example_interfaces/srv/AddTwoInts
# Çıktı:
# int64 a
# int64 b
# ---
# int64 sum

ros2 interface show example_interfaces/action/Fibonacci
# Çıktı:
# int32 order
# ---
# int32[] sequence
# ---
# int32[] partial_sequence

# Doldurulmaya hazır şablon üret (CLI çağrılarında kullanışlı)
ros2 interface proto std_msgs/msg/String
# Çıktı:
# data: ''
```

## 3.3 Genel Tavsiye

"Hangi iletişim türünü seçmeliyim?" sorusunun doğrudan bir cevabı var. Önce şu tabloyu inceleyin:

| Özellik         | Topic | Service | Action |
|-----------------|-------|---------|--------|
| Yanıt garantisi | Hayır | Evet    | Evet   |
| Asenkron        | Evet  | Hayır   | Evet   |
| Süreç takibi    | Hayır | Hayır   | Evet   |
| Çok alıcı       | Evet  | Hayır   | Hayır  |

Pratik kural olarak: sürekli akan veri için **topic** (sensör okumalar, kamera görüntüsü), anlık "sor-cevap al" işlemleri için **service** (parametre sorgulama, basit hesaplamalar), uzun süren ve takip gerektiren görevler için **action** (navigasyon, nesne tutma, multi-adım planlar). Çoğu durumda bir düğümün birden fazla iletişim türünü aynı anda kullandığını göreceksiniz — bu tamamen normaldir.
