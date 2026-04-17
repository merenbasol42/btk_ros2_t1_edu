# ROS Nedir?

ROS, Robot Operating System kelimelerinin baş harflerinden oluşur ve robot işletim sistemi manasına gelir. Ancak ROS gerçek bir işletim sistemi değildir.

Peki o zaman neden ismini ROS koymuşlar?

Çünkü ROS robotik uygulamalar için geliştirilmiş bir **meta-işletim sistemidir**.

- **İşletim sistemi:** Donanım kaynaklarını yöneten ve yazılımların bu kaynakları uyum içinde kullanmasını sağlayan sistemdir.
- **Meta-işletim sistemi:** Gerçek bir işletim sistemi olmamasına rağmen bir işletim sisteminin yaptığı işlerin çoğunu yapabilen (ya da taklit eden) yazılımlardır.

---

## ROS'un Temel (Çekirdek) Özellikleri

ROS, robotik yazılım bileşenleri arasındaki haberleşmeyi, kaynak yönetimini ve modüler yapıyı organize eder. Klasik işletim sistemlerinin çekirdek görevlerini üstlenir; ancak bu görevleri robotik sistemlerin gereksinimlerine uygun şekilde yeniden yorumlar.

| | Haberleşme |
|---|---|
| **OS** | Farklı süreçler (process) arasında veri alışverişi, IPC (Inter-Process Communication), soketler veya mesaj kuyrukları aracılığıyla sağlanır. |
| **ROS** | Farklı düğümler (nodes) arasındaki veri alışverişi, publish/subscribe ve service mekanizmalarıyla yapılır. Böylece süreçler arasında gerçek zamanlı, modüler ve dağıtık iletişim sağlanır. |

| | Paket Yönetimi |
|---|---|
| **OS** | Yazılım bileşenleri, `apt`, `yum` gibi paket yöneticileri ile kurulur ve yönetilir. |
| **ROS** | Yazılım modülleri ROS paketleri olarak düzenlenir ve `rosdep`, `rospack` gibi araçlarla bağımlılıklar yönetilir. Her işlevsel bileşen, bağımsız ama entegre bir yapıda tutulur. |

| | Ortam Değişkenleri |
|---|---|
| **OS** | Ortam değişkenleri, tüm süreçlerin erişebileceği genel ayarları tanımlar (örneğin `PATH`, `HOME`). |
| **ROS** | Parametre sunucusu benzer şekilde sistem genelinde erişilebilen ayarları saklar. Tüm düğümler ortak konfigürasyon değerlerini merkezi bir yerden alabilir. |

| | Başlatma Araçları |
|---|---|
| **OS** | Programlar genellikle bash scriptleri, `systemd` servisleri veya komut dosyalarıyla başlatılır. |
| **ROS** | `roslaunch` veya `ros2 launch` araçları, birden fazla düğümün aynı anda konfigürasyonlu biçimde başlatılmasını sağlar. Sistem bir bütün olarak kolayca ayağa kaldırılabilir. |

| | Donanım Soyutlama |
|---|---|
| **OS** | Donanımlara erişim sürücüler (drivers) ve API'ler aracılığıyla soyutlanır. |
| **ROS** | Donanım bağımlılıkları ROS control, hardware interface veya özel sürücüler aracılığıyla soyutlanır. Robotlar, farklı donanımlar üzerinde aynı yazılımla çalışabilir hale gelir. |

---

## ROS'un Araç Özellikleri

ROS, yalnızca bir haberleşme altyapısı değil; aynı zamanda robotların koordinasyon, gözlemleme ve modelleme süreçlerini destekleyen kapsamlı bir geliştirme ekosistemidir.

### Konumlama

ROS'un `tf` sistemi, farklı bileşenlerin (kamera, sensör vb.) kendi koordinat sistemleri arasındaki uzaysal dönüşümleri yönetir. Böylece bileşenler, birbirlerinin konum ve yönelim bilgisine zaman senkronizasyonu içinde erişebilir. Bu yapı, özellikle hareket planlama ve sensör füzyonu için kritiktir.

### İzleme

ROS; `rqt_graph`, `rosbag` ve `RViz` araçlarıyla sistem yapısını ve verilerini inceleme olanağı sunar.

- **rqt_graph** — veri akışını görselleştirir
- **rosbag** — sensör verilerini kaydeder ve oynatır
- **RViz** — robotu ve çevresini 3D gösterir

### Modelleme

**URDF** (Unified Robot Description Format), robotun fiziksel yapısını XML tabanlı olarak tanımlar. Gövde, eklemler, kütle ve görsel bileşenler bu dosyada yer alır. URDF, simülasyon, görselleştirme ve hareket planlama gibi işlemlerin temelini oluşturur.

---

