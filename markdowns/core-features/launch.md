- [1. Giriş](#1-giriş)
- [2. Teori](#2-teori)
  - [2.1 Launch Sistemi Nedir?](#21-launch-sistemi-nedir)
  - [2.2 Launch Dosyasının Anatomisi](#22-launch-dosyasının-anatomisi)
  - [2.3 Namespace ve Remapping](#23-namespace-ve-remapping)
- [3. Kullanım](#3-kullanım)
  - [3.1 API (Python)](#31-api-python)
    - [LaunchDescription](#launchdescription)
    - [Node](#node)
    - [DeclareLaunchArgument ve LaunchConfiguration](#declarelauncharguement-ve-launchconfiguration)
    - [IncludeLaunchDescription](#includelaunchdescription)
    - [OpaqueFunction](#opaquefunction)
  - [3.2 CLI](#32-cli)
    - [3.3 Genel Tavsiye](#33-genel-tavsiye)
    - [Tam Kullanım Örneği](#tam-kullanım-örneği)

---

## 1. Giriş

`parameters.md`'de her düğümün çalışma zamanında nasıl yapılandırıldığını öğrendiniz; launch sistemi ise bu düğümleri ve parametrelerini tek bir yerden koordineli biçimde ayağa kaldırmanızı sağlar.

Bu dosyayı okuduğunuzda şunları öğrenmiş olacaksınız:

- Python formatında launch dosyası yazma ve bunu `ros2 launch` komutuyla çalıştırma
- Çalışma zamanında argüman alarak farklı ortam konfigürasyonları üretme
- Namespace ve remapping ile düğümleri izole etme ve yönlendirme

Hazırsanız başlayalım.

---

## 2. Teori

### 2.1 Launch Sistemi Nedir?

Launch sistemi (başlatma sistemi), birden fazla ROS2 düğümünü, parametresini ve ortam değişkenini tek bir dosyadan koordineli biçimde başlatmaya yarayan bir yapıdır. Gerçek bir robotik sistemde onlarca düğüm çalışıyor olabilir; her birini ayrı terminalde elle başlatmak yerine launch dosyası tüm bu süreci otomatize eder.

Launch dosyaları Python, XML veya YAML formatında yazılabilir. Bu belgede yalnızca **Python formatına** odaklanacağız; çünkü Python formatı koşullara, değişkenlere ve fonksiyon çağrılarına doğrudan erişim sağlar.

> **Gerçek hayat örneği:** Bir orkestranın şefi, her müzisyene hangi enstrümanı ne zaman çalacağını söyler. Launch dosyası da tam bu rolü üstlenir: hangi düğümün hangi parametreyle, hangi namespace altında başlayacağını tanımlar. Müzisyenler (düğümler) birbirinden habersizdir; yönetimi şef (launch dosyası) üstlenir.

ROS2 launch sisteminin temel bileşenleri şunlardır:

- **`LaunchDescription`** — başlatılacak her şeyin listesini tutan kap
- **`Node`** — tek bir çalıştırılabilir ROS2 düğümünü temsil eder
- **`DeclareLaunchArgument`** — dışarıdan alınacak argümanı tanımlar
- **`LaunchConfiguration`** — tanımlanmış argümanın değerini okur
- **`IncludeLaunchDescription`** — başka bir launch dosyasını içe aktarır
- **`OpaqueFunction`** — Python kodu çalıştırarak dinamik eylemler üretir

### 2.2 Launch Dosyasının Anatomisi

Her Python launch dosyasında `generate_launch_description()` adlı bir fonksiyon bulunmak **zorundadır**. `ros2 launch` komutu bu fonksiyonu çağırır ve dönen `LaunchDescription` nesnesini işleme alır.

```python
from launch import LaunchDescription

def generate_launch_description():
    return LaunchDescription([
        # eylemler buraya gelir
    ])
```

Launch dosyaları genellikle paketinizin `launch/` dizinine yerleştirilir ve `setup.py`'de `data_files` aracılığıyla kuruluma eklenir:

```python
# setup.py içinde
data_files=[
    ('share/' + package_name + '/launch', glob('launch/*.py')),
],
```

> **Gerçek hayat örneği:** `generate_launch_description()` bir restoranın günlük menüsüdür. Müşteri (ros2 launch) gelip menüyü ister; mutfak (ROS2 runtime) menüde yazan her şeyi sırayla hazırlar.

### 2.3 Namespace ve Remapping

**Namespace** (isim alanı), bir düğümün ve onun ürettiği tüm topic/servis isimlerinin önüne eklenen bir ön ektir. Aynı düğümden birden fazla örnek çalıştırmak istediğinizde her birini farklı bir namespace altına alarak isim çakışmasını önlemiş olursunuz.

**Remapping** (yeniden eşleme) ise bir düğümün kullandığı topic veya servis ismini dışarıdan değiştirmenizi sağlar. Düğümün kaynak koduna dokunmadan `/scan` topic'ini `/lidar/scan` olarak yönlendirebilirsiniz.

> **Gerçek hayat örneği:** Namespace bir bina numarası gibidir. İki ayrı binada aynı isimli "101 nolu oda" olabilir; hangi binada olduğunu belirtmezseniz hangisini kastettiğiniz belirsiz kalır. Remapping ise odanın kapı numarasına yeni bir isim etiketi yapıştırmak gibidir — oda değişmez, yalnızca adı değişir.

Namespace kuralları:

- Namespace `/` ile başlamaz, sonda `/` olmaz
- Namespace altındaki topic isimleri otomatik olarak `/<namespace>/<topic>` biçimini alır
- Bir düğüme hem namespace hem remapping uygulanabilir; önce namespace eklenir, sonra remapping işlenir

---

## 3. Kullanım

### 3.1 API (Python)

#### LaunchDescription

```python
from launch import LaunchDescription

LaunchDescription(initial_entities=None)
```

| Parametre | Tür | Açıklama |
|---|---|---|
| `initial_entities` | `list` veya `None` | Başlatılacak `Action` nesnelerinin listesi |

`LaunchDescription`, `generate_launch_description()` fonksiyonunun döndürdüğü nesnedir. İçindeki tüm eylemler sırayla işleme alınır ancak bu sıra, düğümlerin başlangıç zamanını garanti etmez.

```python
return LaunchDescription([
    node_a,
    node_b,
    declared_arg,
])
```

#### Node

```python
from launch_ros.actions import Node

Node(
    package,
    executable,
    name=None,
    namespace='',
    parameters=None,
    remappings=None,
    arguments=None,
    output='log',
)
```

| Parametre | Tür | Açıklama |
|---|---|---|
| `package` | `str` | Düğümü içeren paketin adı |
| `executable` | `str` | Çalıştırılacak dosya adı (`setup.py`'deki entry point) |
| `name` | `str` | Düğümün çalışma zamanı adı (isteğe bağlı) |
| `namespace` | `str` | Düğümün namespace'i |
| `parameters` | `list` | Sözlük veya YAML dosya yollarından oluşan liste |
| `remappings` | `list[tuple]` | `(eski_isim, yeni_isim)` çiftlerinden oluşan liste |
| `arguments` | `list` | Düğüme iletilen komut satırı argümanları |
| `output` | `str` | `'log'`, `'screen'` veya `'both'` |

`output='screen'` yapılandırılırsa düğümün stdout/stderr çıktısı terminale yansır; `'log'` yapılandırılırsa yalnızca dosyaya yazılır.

```python
Node(
    package='turtlesim',
    executable='turtlesim_node',
    name='sim',
    namespace='robot1',
    parameters=[{'background_r': 100}],
    remappings=[('/turtle1/cmd_vel', '/cmd_vel')],
    output='screen',
)
```

#### DeclareLaunchArgument ve LaunchConfiguration

```python
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

DeclareLaunchArgument(name, default_value=None, description='')
LaunchConfiguration(variable_name)
```

| Parametre | Tür | Açıklama |
|---|---|---|
| `name` | `str` | Argümanın adı |
| `default_value` | `str` | Kullanıcı değer vermezse kullanılacak değer |
| `description` | `str` | `ros2 launch --show-args` çıktısında görünen açıklama |

`DeclareLaunchArgument` argümanı **tanımlar**; `LaunchConfiguration` ise bu argümanın **değerini** okur. İkisi birlikte kullanılmak zorundadır.

```python
use_sim_time_arg = DeclareLaunchArgument(
    'use_sim_time',
    default_value='false',
    description='Simülasyon saatini etkinleştir',
)

node = Node(
    package='my_pkg',
    executable='my_node',
    parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
)
```

`LaunchConfiguration` nesnesi bir `Substitution`'dır; değeri launch anında çözümlenir, Python kodu çalışırken değil. Bu nedenle onu doğrudan `if` ifadesinde kullanamazsınız — bunun için `OpaqueFunction` kullanın.

#### IncludeLaunchDescription

```python
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

IncludeLaunchDescription(
    launch_description_source,
    launch_arguments=None,
)
```

| Parametre | Tür | Açıklama |
|---|---|---|
| `launch_description_source` | `LaunchDescriptionSource` | İçe aktarılacak launch dosyasının kaynağı |
| `launch_arguments` | `dict` | Alt launch dosyasına iletilecek argümanlar |

Büyük sistemlerde her alt sistem kendi launch dosyasını yönetir; üst düzey dosya bunları `IncludeLaunchDescription` ile bir araya getirir.

```python
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

nav_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
        os.path.join(
            get_package_share_directory('nav2_bringup'),
            'launch', 'navigation_launch.py',
        )
    ),
    launch_arguments={'use_sim_time': 'true'}.items(),
)
```

#### OpaqueFunction

```python
from launch.actions import OpaqueFunction

OpaqueFunction(function=callable)
```

| Parametre | Tür | Açıklama |
|---|---|---|
| `function` | `callable` | `(context, *args, **kwargs) -> list[Action]` imzasına sahip fonksiyon |

`OpaqueFunction`, launch grafiğinin çalışma zamanında çözümlenmesi gereken koşullu mantık içerdiğinde kullanılır. Fonksiyon, `LaunchContext` nesnesine erişerek `LaunchConfiguration` değerlerini gerçek Python string'lerine dönüştürebilir.

```python
from launch.actions import OpaqueFunction
from launch.substitutions import LaunchConfiguration

def launch_setup(context, *args, **kwargs):
    robot_model = LaunchConfiguration('robot_model').perform(context)

    if robot_model == 'differential':
        node = Node(package='base_ctrl', executable='diff_drive')
    else:
        node = Node(package='base_ctrl', executable='omni_drive')

    return [node]


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('robot_model', default_value='differential'),
        OpaqueFunction(function=launch_setup),
    ])
```

`OpaqueFunction` içindeki Python kodu normal `if/else` yazmanıza izin verir; ancak bu fonksiyon launch anında çalıştığından, derleme aşamasında değil çalışma zamanında hata verir.

---

### 3.2 CLI

```bash
# Bir paketteki launch dosyasını çalıştır
ros2 launch turtlesim multisim.launch.py
```
```
[INFO] [launch]: All log files can be found below /home/user/.ros/log/...
[INFO] [turtlesim_node-1]: process started with pid [12345]
[INFO] [turtlesim_node-2]: process started with pid [12346]
```

```bash
# Launch dosyasının kabul ettiği argümanları listele
ros2 launch nav2_bringup navigation_launch.py --show-args
```
```
Arguments (pass arguments as '<name>:=<value>'):

    'use_sim_time':
        Simülasyon saatini etkinleştir
        (default: 'false')

    'map':
        Harita YAML dosyasının tam yolu
        (default: '')
```

```bash
# Argüman geçerek launch dosyasını çalıştır
ros2 launch my_pkg bringup.launch.py use_sim_time:=true robot_model:=omni
```
```
[INFO] [launch]: All log files can be found below /home/user/.ros/log/...
[INFO] [my_node-1]: process started with pid [13579]
```

```bash
# Çalışan düğümleri kontrol et (launch çalışırken başka terminalde)
ros2 node list
```
```
/robot1/sim
/robot1/controller
/diagnostics
```

---

### 3.3 Genel Tavsiye

| Kriter | Tek Node() | IncludeLaunchDescription | OpaqueFunction |
|---|---|---|---|
| Kullanım amacı | Tek bir düğüm başlatma | Alt sistemi dahil etme | Koşullu düğüm seçimi |
| Python koşullu mantık | Hayır | Kısmi (argüman iletimi) | Evet, tam erişim |
| Karmaşıklık | Düşük | Orta | Yüksek |
| Bakım kolaylığı | Yüksek | Yüksek | Orta |
| `LaunchConfiguration` değerini `if`'te kullanma | Hayır | Hayır | Evet (`context.perform`) |

Bir launch dosyasında yalnızca sabit konfigürasyonlarla birkaç düğüm başlatacaksanız düz `Node()` listesi yeterlidir. Projeniz büyüdükçe her alt sistemi kendi launch dosyasına taşıyın ve bunları `IncludeLaunchDescription` ile birleştirin; bu yaklaşım hem test edilebilirliği hem de yeniden kullanılabilirliği artırır. `OpaqueFunction`'ı yalnızca `LaunchConfiguration` değerini gerçek Python koşullarında değerlendirmeniz gerektiğinde kullanın — örneğin robot modeline göre farklı bir düğüm başlatmak ya da argümana göre farklı parametre dosyaları seçmek. Çoğu durumda `IncludeLaunchDescription` ile argüman geçmek `OpaqueFunction`'ın esnekliğine ihtiyaç duymadan yeterli esnekliği sağlar.

---

#### Tam Kullanım Örneği

Aşağıdaki launch dosyası bu belgede anlatılan tüm yapıları gerçekçi bir senaryo üzerinde bir arada gösterir. Senaryo: iki tekerlekli diferansiyel bir mobil robot için algılama ve navigasyon düğümlerini başlat; robot modeli argümana göre seçilsin, her iki alt sistem de kendi namespace'i altında çalışsın.

**Dizin yapısı:**

```
my_robot_bringup/
├── launch/
│   └── bringup.launch.py      ← bu dosya
├── config/
│   └── robot_params.yaml
└── setup.py
```

**`launch/bringup.launch.py`:**

```python
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


# --- 1. Bölüm: OpaqueFunction ile çalışacak kurulum fonksiyonu ---

def launch_setup(context, *args, **kwargs):
    # LaunchConfiguration değerlerini Python string'ine dönüştür
    use_sim_time = LaunchConfiguration('use_sim_time').perform(context)
    robot_model  = LaunchConfiguration('robot_model').perform(context)

    pkg_share = get_package_share_directory('my_robot_bringup')
    params_file = os.path.join(pkg_share, 'config', 'robot_params.yaml')

    # --- 2. Bölüm: Robot modeline göre tabana ait sürücü düğümünü seç ---

    if robot_model == 'differential':
        base_driver = Node(
            package='base_drivers',
            executable='diff_drive_node',
            name='base_driver',
            namespace='base',                          # /base/... altında yayın yapar
            parameters=[
                params_file,
                {'use_sim_time': use_sim_time == 'true'},
            ],
            remappings=[
                ('cmd_vel', '/cmd_vel'),               # namespace dışından komut al
            ],
            output='screen',
        )
    else:
        base_driver = Node(
            package='base_drivers',
            executable='omni_drive_node',
            name='base_driver',
            namespace='base',
            parameters=[
                params_file,
                {'use_sim_time': use_sim_time == 'true'},
            ],
            remappings=[
                ('cmd_vel', '/cmd_vel'),
            ],
            output='screen',
        )

    # --- 3. Bölüm: Sabit düğümler (model bağımsız) ---

    lidar_node = Node(
        package='rplidar_ros',
        executable='rplidar_node',
        name='lidar',
        namespace='sensors',                           # /sensors/scan olarak yayınlar
        parameters=[{'use_sim_time': use_sim_time == 'true'}],
        remappings=[
            ('scan', 'scan'),                          # /sensors/scan → değişmez
        ],
        output='log',
    )

    # --- 4. Bölüm: Başka bir paketten navigasyon launch dosyasını dahil et ---

    nav_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('nav2_bringup'),
                'launch', 'navigation_launch.py',
            )
        ),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'params_file':  params_file,
        }.items(),
    )

    return [base_driver, lidar_node, nav_launch]


# --- 5. Bölüm: Zorunlu giriş noktası ---

def generate_launch_description():
    return LaunchDescription([
        # Argümanlar her zaman önce tanımlanır
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Simülasyon saatini etkinleştir (Gazebo ile kullanım için)',
        ),
        DeclareLaunchArgument(
            'robot_model',
            default_value='differential',
            description='Taban sürücüsü türü: differential veya omni',
        ),

        # OpaqueFunction geri kalan her şeyi bağlamı okuyarak kurar
        OpaqueFunction(function=launch_setup),
    ])
```

**Dosyanın akışı adım adım:**

1. `ros2 launch my_robot_bringup bringup.launch.py` çağrıldığında ROS2, `generate_launch_description()` fonksiyonunu çalıştırır.
2. İki `DeclareLaunchArgument` eylemi kayıt altına alınır; kullanıcı argüman geçmediyse varsayılan değerler (`false`, `differential`) etkinleşir.
3. `OpaqueFunction`, `launch_setup` fonksiyonunu `LaunchContext` ile çağırır.
4. `launch_setup` içinde her iki `LaunchConfiguration` değeri `.perform(context)` ile gerçek stringe dönüştürülür ve `if/else` koşulu değerlendirilebilir hale gelir.
5. `robot_model == 'differential'` koşuluna göre `diff_drive_node` veya `omni_drive_node` seçilir.
6. `lidar_node` ve `nav_launch` model bağımsız olduğundan her durumda oluşturulur.
7. Fonksiyon üç eylemi liste olarak döndürür; ROS2 bunları paralel biçimde başlatır.

**Çalıştırma örnekleri:**

```bash
# Varsayılan değerlerle (diferansiyel, simülasyon kapalı)
ros2 launch my_robot_bringup bringup.launch.py

# Omni tekerlekli robot, Gazebo simülasyonu açık
ros2 launch my_robot_bringup bringup.launch.py robot_model:=omni use_sim_time:=true
```
