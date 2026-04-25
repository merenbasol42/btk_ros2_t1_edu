# Plan: ROS2 Kitapçığının Tamamlanması

## Context

BTK Akademi atölyesi için Türkçe ROS2 eğitim kitapçığı yazılıyor. Kitapçığın amacı robotik sistemlere giriş için teorik altyapı vermek ve ROS2'nin temel CLI/API kullanımlarını öğretmek. Anlatım cookbook değil teorik/kavramsal olmalı.

**Stil şablonu (her agent bu kurallara uyar):**
- Türkçe; teknik terimler ilk geçişte (İngilizce) şeklinde parantez içinde
- "Siz" hitabı, samimi ama resmi ton
- Her ana kavram için `> **Gerçek hayat örneği:**` bloğu zorunlu
- Karşılaştırmalar tablo olarak (örn. ROS1 vs ROS2)
- Belge yapısı: İçindekiler → Giriş → Teori → Kullanım (API + CLI + Genel Tavsiye)
- Cookbook değil teorik anlatım — adım adım talimat değil, kavramsal derinlik
- Kod örnekleri: tam node boilerplate değil, kritik parçalar
- API bölümünde fonksiyon imzaları parametre tablosuyla gösterilir
- "Genel Tavsiye" bölümünde karar tablosu bulunur
- CLI örneklerinde beklenen çıktı gösterilir

---

## Kitap Nihai Yapısı

```
1. Giriş: Robotik Sistemler ve ROS
   1.1 Robotik Sistemler Nedir?
   1.2 ROS'un Robotik Sistemlerdeki Pozisyonu
   1.3 ROS Nedir?
   1.4 ROS'tan ROS2'ye

2. Paketler ve Çalışma Alanları

3. İletişim — Topic, Service, Action

4. Parametreler

5. Launch Sistemi

6. Gözlem Araçları — rqt, rosbag2, RViz

7. Modelleme — URDF

8. Koordinasyon — tf2
```

---

## Yürütme Sırası

WP1 → WP2 → WP3 → WP4 → WP5 → WP6 (sıralı, her biri bir önceki bittikten sonra başlar)

---

## İş Paketleri

### WP1: Giriş Bölümü — Robotik Sistemler ve ROS'un Evrimi

**Hedef dosya:** `markdowns/introduction-to-robotic-system-with-ros2.md`  
**Sıra:** 1

**Prompt:**

```
ROS2 ile Robotik Sistemlere Giriş kitapçığının giriş bölümünü yazacaksın.
Bu bir BTK Akademi atölyesi için Türkçe eğitim kitapçığı.

Giriş bölümü şu bölümleri içermeli:

---

**1. Robotik Sistemler Nedir?** 

Teorik açıklama. Şunları kapsasın:
- Robot tanımı: fiziksel dünyayı algılayan, işleyen, etkileyen otonom/yarı-otonom sistem
- Robotik sistemin katmanları: algılama (sensing) → işleme (computation) → eylem (actuation)
- Gerçek hayat analojisi: insan sinir sistemi ile karşılaştırma (duyu organları → beyin → kaslar)
- Robotik sistemlerde yazılımın önemi: donanım artık ucuz, fark yazılımda

**2. ROS'un Robotik Sistemlerdeki Pozisyonu** (~500 kelime)

Teorik konumlandırma. Şunları kapsasın:
- Robotik yazılımda ortak sorunlar: her takım aynı tekerleği yeniden icat ediyor
- ROS'tan önce ve sonra: soyutlama katmanının önemi
- ROS'un ekosistem içindeki yeri: işletim sistemi üzerinde, uygulama altında
- Neden standart bir middleware? Yeniden kullanım, topluluk, hız

**3. ROS Nedir?** 

Kavramsal tanım. Şunları kapsasın:
- Meta-işletim sistemi (meta-OS) kavramı: işletim sistemi değil, üzerine oturur
- Node, topic, service, action kavramlarına kısa giriş (detay sonraki bölümlerde)
- ROS'un sağladığı araç ekosistemi: build sistemi, debug araçları, simülasyon

**4. ROS'tan ROS2'ye** 

Teorik/tarihsel geçiş. Şunları kapsasın:
- ROS1'in sınırlılıkları: tek master, gerçek zamanlı destek yok, güvenlik yok, Windows yok
- ROS2'nin mimarisi: DDS (Data Distribution Service) üzerine kurulu, merkezi master yok
- DDS nedir? Kısa teorik açıklama — endüstriyel standart middleware
- ROS2'nin öne çıkan özellikleri: çoklu platform, QoS, güvenlik, lifecycle nodes
- Gerçek hayat analojisi: ROS1 merkezi bir posta ofisi gibi (her şey tek noktadan geçer),
  ROS2 dağıtık bir kurye ağı gibi (peer-to-peer)
- ROS1 vs ROS2 karşılaştırma tablosu (zorunlu)

---

Yazım kuralları:
- Türkçe, teknik terimler ilk geçişte (İngilizce) şeklinde parantez içinde
- "Siz" hitabı, samimi ama resmi
- Her ana kavram için `> **Gerçek hayat örneği:**` bloğu
- Cookbook değil teorik anlatım — adım adım değil, kavramsal derinlik

Çıktıyı `markdowns/introduction-to-robotic-system-with-ros2.md` dosyasına yaz.

---

**Progress takibi:**
İçeriği yazdıktan sonra `markdowns/progress.md` dosyasını kontrol et.
- Dosya yoksa oluştur, içine aşağıdaki tabloyu yaz:

| WP  | Başlık                        | Hedef Dosya                                           | Durum           |
|-----|-------------------------------|-------------------------------------------------------|-----------------|
| WP1 | Giriş Bölümü                  | markdowns/introduction-to-robotic-system-with-ros2.md | ⬜ Bekliyor     |
| WP2 | Paketler ve Çalışma Alanları  | markdowns/introduction-to-robotic-system-with-ros2.md | ⬜ Bekliyor     |
| WP3 | Parametreler                  | markdowns/introduction-to-robotic-system-with-ros2.md | ⬜ Bekliyor     |
| WP4 | Gözlem Araçları               | markdowns/introduction-to-robotic-system-with-ros2.md | ⬜ Bekliyor     |
| WP5 | Modelleme — URDF              | markdowns/introduction-to-robotic-system-with-ros2.md | ⬜ Bekliyor     |
| WP6 | Koordinasyon — tf2            | markdowns/introduction-to-robotic-system-with-ros2.md | ⬜ Bekliyor     |

- Sonra WP1 satırındaki `⬜ Bekliyor`'u `✅ Tamamlandı` ile değiştir.
```

---

### WP2: Paketler ve Çalışma Alanları

**Hedef dosya:** `markdowns/introduction-to-robotic-system-with-ros2.md`
**Sıra:** 2

**Prompt:**

```
ROS2 ile Robotik Sistemlere Giriş kitapçığı için "Paketler ve Çalışma Alanları" bölümünü yazacaksın.
Bu bir BTK Akademi atölyesi için Türkçe eğitim kitapçığı.

Belge yapısını uygula: İçindekiler → Giriş → Teori → Kullanım (API + CLI + Genel Tavsiye)

---

**Teori bölümü şunları kapsamalı:**

2.1 Çalışma Alanı (Workspace) Kavramı
- Workspace nedir? Bir veya birden fazla paketin geliştirildiği dizin ortamı
- Dizin yapısı: src/ (kaynak), build/ (derleme çıktıları), install/ (kurulum), log/ (loglar)
- Overlay/underlay kavramı: çalışma alanları birbirini katmanlı olarak genişletebilir
- Gerçek hayat analojisi: proje klasörü — ham belgeler (src), taslaklar (build), son ürün (install)

2.2 ROS2 Paketi Nedir?
- Paketin tanımı: belirli bir işlevi gerçekleştiren, bağımsız dağıtılabilir birim
- package.xml anatomisi: name, version, description, maintainer, depend blokları
- Python paketi için setup.py ve setup.cfg
- ament_python vs ament_cmake: Python ve C++ paketleri için farklı build sistemi
- Gerçek hayat analojisi: npm paketi veya pip paketi — bağımlılıkları bildirir, kurulabilir birim

2.3 Derleme Sistemi — colcon
- colcon nedir? ROS2'nin meta-build aracı
- Seçici derleme: --packages-select ile sadece belirli paketi derle
- Kurulum kaynağı: install/setup.bash neden source edilmeli?
- Gerçek hayat analojisi: make/cmake gibi ama çoklu paket için orkestra şefi

---

**Kullanım bölümü şunları kapsamalı:**

3.1 API (Python)
- setup.py: entry_points ile executable tanımlama
- package.xml: <exec_depend> ile çalışma zamanı bağımlılıkları
- Fonksiyon imzaları ve parametre tabloları

3.2 CLI
- `ros2 pkg create --build-type ament_python my_package`
- `colcon build --packages-select my_package`
- `source install/setup.bash`
- `ros2 pkg list` ve `ros2 pkg prefix`
- `ros2 run package_name executable_name`

3.3 Genel Tavsiye
- Hangi durumda ament_python, hangi durumda ament_cmake?
- Workspace overlay ne zaman kullanılır?
- Karar tablosu

---

Yazım kuralları:
- Türkçe, teknik terimler ilk geçişte (İngilizce) şeklinde parantez içinde
- Her ana kavram için `> **Gerçek hayat örneği:**` bloğu
- Cookbook değil teorik — adım adım talimat değil, kavramsal derinlik
- Kod örnekleri: tam node boilerplate değil, kritik parçalar
- API fonksiyonları parametre tablosuyla gösterilir
- "Genel Tavsiye" bölümünde karar tablosu bulunur
- CLI örneklerinde beklenen çıktı gösterilir

Çıktıyı `markdowns/introduction-to-robotic-system-with-ros2.md` dosyasına ekle (mevcut içeriğin sonuna yeni bölüm olarak).

**Progress takibi:** İçeriği yazdıktan sonra `markdowns/progress.md` dosyasını aç, WP2 satırındaki `⬜ Bekliyor`'u `✅ Tamamlandı` ile değiştir.
```

---

### WP3: Parametreler

**Hedef dosya:** `markdowns/introduction-to-robotic-system-with-ros2.md`
**Sıra:** 3

**Prompt:**

```
ROS2 ile Robotik Sistemlere Giriş kitapçığı için "Parametreler" bölümünü yazacaksın.
Bu bir BTK Akademi atölyesi için Türkçe eğitim kitapçığı.

Belge yapısını uygula: İçindekiler → Giriş → Teori → Kullanım (API + CLI + Genel Tavsiye)

---

**Teori bölümü şunları kapsamalı:**

2.1 Parametre Sunucusu (Parameter Server) Kavramı
- Parametre nedir? Nodes'ların davranışını etkileyen yapılandırma değerleri
- Hardcode vs parametre: neden değerleri kod içine gömmemeli?
- ROS2'de parametreler node'a aittir (ROS1'den fark: global parametre sunucusu yok)
- Desteklenen tipler: bool, int, float, string, byte_array, list türleri
- Gerçek hayat analojisi: uygulamanın .env dosyası — kodu değiştirmeden davranışı ayarla

2.2 Parametre Yaşam Döngüsü
- Bildirim (declare): node başlarken hangi parametrelerin kullanılacağı tanımlanır
- Okuma (get): çalışma sırasında değer okunur
- Güncelleme (set): dışarıdan veya callback ile değer değiştirilebilir
- Callback mekanizması: parametre değişince node ne yapmalı?

2.3 YAML ile Yapılandırma
- Parametre dosyaları: neden YAML?
- Namespace hiyerarşisi: node_name.ros__parameters yapısı
- Launch dosyasıyla entegrasyon: parametreler launch sırasında node'a aktarılabilir

---

**Kullanım bölümü şunları kapsamalı:**

3.1 API (Python) — rclpy.node.Node metodları
- `declare_parameter(name, value, descriptor=None)` → parametre tanımlama
- `get_parameter(name)` → ParameterValue döner
- `set_parameters([Parameter(...)])` → liste ile toplu güncelleme
- `add_on_set_parameters_callback(callback)` → değişim callback'i
- Parametre tabloları ve kritik notlar

3.2 CLI
- `ros2 param list /node_name`
- `ros2 param get /node_name param_name`
- `ros2 param set /node_name param_name value`
- `ros2 param dump /node_name` → YAML çıktısı
- `ros2 param load /node_name params.yaml`

3.3 Genel Tavsiye
- Parametre vs topic: ne zaman hangisi kullanılır?
- Statik yapılandırma vs dinamik güncelleme
- Karar tablosu

---

Yazım kuralları:
- Türkçe, teknik terimler ilk geçişte (İngilizce) şeklinde
- Her ana kavram için `> **Gerçek hayat örneği:**` bloğu
- Cookbook değil teorik anlatım
- API fonksiyonları parametre tablosuyla gösterilir
- "Genel Tavsiye" bölümünde karar tablosu bulunur
- CLI örneklerinde beklenen çıktı gösterilir

Çıktıyı `markdowns/introduction-to-robotic-system-with-ros2.md` dosyasına ekle (mevcut içeriğin sonuna yeni bölüm olarak).

**Progress takibi:** İçeriği yazdıktan sonra `markdowns/progress.md` dosyasını aç, WP3 satırındaki `⬜ Bekliyor`'u `✅ Tamamlandı` ile değiştir.
```

---

### WP4: Gözlem Araçları

**Hedef dosya:** `markdowns/introduction-to-robotic-system-with-ros2.md`
**Sıra:** 4

**Prompt:**

```
ROS2 ile Robotik Sistemlere Giriş kitapçığı için "Gözlem Araçları" bölümünü yazacaksın.
Bu bir BTK Akademi atölyesi için Türkçe eğitim kitapçığı.

Belge yapısını uygula. Bu bölümde "Teori" ağırlıklı olacak,
API bölümü daha kısa — gözlem araçları ağırlıklı olarak CLI üzerinden kullanılır.

---

**Teori bölümü şunları kapsamalı:**

2.1 Sistem Gözleminin Önemi
- Çalışan bir sistemi anlamak: hangi node'lar var, ne mesaj alıp veriyor?
- Debug döngüsü: gözlem → hipotez → doğrulama
- Gerçek hayat analojisi: bir fabrikadaki denetim odası — sensörler, göstergeler, loglar

2.2 rqt — Grafik Araç Ekosistemi
- rqt_graph: sistemin iletişim topolojisini görselleştirme (node'lar ve topic'ler)
- rqt_plot: sayısal verilerin gerçek zamanlı grafiği
- rqt_console: log mesajlarını filtreleyerek izleme
- Plugin mimarisi: rqt aslında bir çerçeve, araçlar plugin olarak eklenir

2.3 rosbag2 — Veri Kaydı ve Oynatma
- Bag dosyası nedir? Topic mesajlarının zaman damgalı kaydı
- Neden önemli? Gerçek sensör verisini tekrar oynatarak geliştirme ve test
- Kayıt formatı: SQLite3 veya MCAP (sıkıştırılmış, indekslenmiş)
- Gerçek hayat analojisi: uçuş kaydedici (black box) — olayları sonradan analiz et

2.4 RViz — 3D Görselleştirme
- RViz nedir? Robot durumunu, sensör verilerini, haritaları 3D görselleştiren araç
- Display türleri: RobotModel, LaserScan, PointCloud2, TF, Path vb.
- Config dosyaları: .rviz formatı, kalıcı görselleştirme ayarları
- Gerçek hayat analojisi: kokpit ekranı — gerçek zamanlı sistemin görsel temsili

---

**Kullanım bölümü şunları kapsamalı:**

3.1 API (Python) — sadece rosbag2 için kısa
- rosbag2_py ile Python'dan bag okuma/yazma (kısa, sadece kavramsal)

3.2 CLI (ağırlıklı bölüm)
- rqt_graph: `ros2 run rqt_graph rqt_graph`
- rosbag2: `ros2 bag record -a`, `ros2 bag record /topic1 /topic2`, `ros2 bag play bag_name`, `ros2 bag info bag_name`
- RViz: `rviz2`, `rviz2 -d config.rviz`
- Çıktı örnekleri ile

3.3 Genel Tavsiye
- Hangi araç hangi durumda? (hızlı debug → rqt_graph, veri analizi → rosbag2, robot durumu → RViz)
- Karar tablosu

---

Yazım kuralları:
- Türkçe, teknik terimler ilk geçişte (İngilizce) şeklinde
- Her araç için `> **Gerçek hayat örneği:**` bloğu
- Teorik ağırlık, cookbook değil
- CLI örneklerinde beklenen çıktı gösterilir
- "Genel Tavsiye" bölümünde karar tablosu bulunur

Çıktıyı `markdowns/introduction-to-robotic-system-with-ros2.md` dosyasına ekle (mevcut içeriğin sonuna yeni bölüm olarak).

**Progress takibi:** İçeriği yazdıktan sonra `markdowns/progress.md` dosyasını aç, WP4 satırındaki `⬜ Bekliyor`'u `✅ Tamamlandı` ile değiştir.
```

---

### WP5: Modelleme — URDF

**Hedef dosya:** `markdowns/introduction-to-robotic-system-with-ros2.md`
**Sıra:** 5

**Prompt:**

```
ROS2 ile Robotik Sistemlere Giriş kitapçığı için "Modelleme" bölümünü yazacaksın.
Bu bir BTK Akademi atölyesi için Türkçe eğitim kitapçığı.

Belge yapısını uygula. Bu bölümde API kısmı XML sözdizimi olacak (Python değil).

---

**Teori bölümü şunları kapsamalı:**

2.1 Robot Modelinin Önemi
- Simülasyon, görselleştirme, planlama hepsi modele dayanır
- Geometrik ve dinamik model ayrımı: şekil vs fizik
- Gerçek hayat analojisi: mimari plan — binanın kendisi değil, temsili

2.2 URDF — Unified Robot Description Format
- URDF nedir? XML tabanlı robot tanımlama formatı
- İki temel kavram: link (katı cisim) ve joint (eklem bağlantısı)
- Link özellikleri: visual (görsel), collision (çarpışma), inertial (atalet)
- Joint türleri: fixed, revolute, prismatic, continuous, floating, planar
- URDF ağacı: robot tek bir kök link'ten dallanan ağaç yapısı
- Gerçek hayat analojisi: insan iskeleti — kemikler (link) ve eklemler (joint)

2.3 robot_state_publisher ve joint_state_publisher
- robot_state_publisher: URDF'yi parse eder, tf2 frame'lerini yayınlar
- joint_state_publisher: eklem açılarını simüle eder (geliştirme aşamasında)
- İkisi birlikte: RViz'de hareketli robot görselleştirmesi

2.4 Xacro — URDF Makro Sistemi
- Xacro nedir? XML macro dili — URDF'yi parametrik ve modüler yapar
- <xacro:property>, <xacro:macro> ile tekrar kullanım
- Neden Xacro? Büyük robotlarda URDF yüzlerce satıra çıkar, Xacro bunu yönetilebilir kılar
- Gerçek hayat analojisi: HTML şablonu — aynı yapıyı parametrelerle çoğalt

---

**Kullanım bölümü şunları kapsamalı:**

3.1 "API" — URDF/Xacro XML sözdizimi
- Temel URDF yapısı: <robot>, <link>, <joint> etiketleri
- Joint tanımı: <origin>, <axis>, <limit> elemanları
- Xacro makro tanımı ve kullanımı
- Parametreli link örneği

3.2 CLI
- `check_urdf robot.urdf` — syntax doğrulama
- `urdf_to_graphviz robot.urdf` — bağlantı grafiği
- `ros2 param get /robot_state_publisher robot_description`
- RViz'de RobotModel display ekleme

3.3 Genel Tavsiye
- Ne zaman URDF, ne zaman Xacro kullanılmalı?
- SDF (Gazebo formatı) ile URDF farkı — kısa not
- Karar tablosu

---

Yazım kuralları:
- Türkçe, teknik terimler ilk geçişte (İngilizce) şeklinde
- Her ana kavram için `> **Gerçek hayat örneği:**` bloğu
- Teorik ağırlık, cookbook değil
- CLI örneklerinde beklenen çıktı gösterilir
- "Genel Tavsiye" bölümünde karar tablosu bulunur

Çıktıyı `markdowns/introduction-to-robotic-system-with-ros2.md` dosyasına ekle (mevcut içeriğin sonuna yeni bölüm olarak).

**Progress takibi:** İçeriği yazdıktan sonra `markdowns/progress.md` dosyasını aç, WP5 satırındaki `⬜ Bekliyor`'u `✅ Tamamlandı` ile değiştir.
```

---

### WP6: Koordinasyon — tf2

**Hedef dosya:** `markdowns/introduction-to-robotic-system-with-ros2.md`
**Sıra:** 6

**Prompt:**

```
ROS2 ile Robotik Sistemlere Giriş kitapçığı için "Koordinasyon — tf2" bölümünü yazacaksın.
Bu bir BTK Akademi atölyesi için Türkçe eğitim kitapçığı.

Belge yapısını uygula: İçindekiler → Giriş → Teori → Kullanım (API + CLI + Genel Tavsiye)

---

**Teori bölümü şunları kapsamalı:**

2.1 Koordinat Dönüşümlerinin Önemi
- Robotik sistemde birden fazla referans çerçevesi: dünya, robot gövdesi, sensörler, kollar
- Aynı nesnenin farklı çerçevelerdeki koordinatları neden farklıdır?
- Problemi elle çözme çabası vs otomatik dönüşüm
- Gerçek hayat analojisi: GPS koordinatı (dünya çerçevesi) vs araç içi kamera görüntüsü (araç çerçevesi) — aynı nesne, farklı bakış açısı

2.2 tf2 — Transform Library
- tf2 nedir? ROS2'nin koordinat dönüşüm kütüphanesi
- Frame nedir? Bir koordinat referans sistemi (genellikle sağ el kuralı, Z yukarı)
- Frame ağacı (TF tree): frame'ler parent-child ilişkisiyle bağlı ağaç yapısı
- Zaman damgalı dönüşümler: tf2 her dönüşümü zamanla birlikte saklar — geçmişe dönük sorgulama mümkün
- Standart frame'ler: map, odom, base_link, base_footprint, sensor_frame
- Gerçek hayat analojisi: şehir haritası — her mahallenin kendi koordinat sistemi var, harita hepsini birleştiriyor

2.3 Broadcaster ve Listener
- TransformBroadcaster: "ben bu frame'in pozisyonunu biliyorum" → tf ağacına yayınlar
- StaticTransformBroadcaster: sabit dönüşümler için (sensör montaj pozisyonu gibi)
- TransformListener + Buffer: "bu frame şu an nerede?" → ağaçtan sorgular
- Lookup zaman penceresi: future ve past sorgular, timeout

2.4 tf2 ve robot_state_publisher İlişkisi
- robot_state_publisher URDF'yi okur, eklem açılarından tf frame'lerini otomatik hesaplar
- tf2 altta yatan mekanizma, robot_state_publisher üst katman uygulama

---

**Kullanım bölümü şunları kapsamalı:**

3.1 API (Python) — tf2_ros
- `TransformBroadcaster(node)` + `sendTransform(TransformStamped)`
- `StaticTransformBroadcaster(node)`
- `Buffer()` + `TransformListener(buffer, node)`
- `buffer.lookup_transform(target_frame, source_frame, time)` → TransformStamped döner
- `buffer.transform(stamped_msg, target_frame)` → mesajı dönüştür
- Parametre tabloları ve istisna durumları (LookupException, ExtrapolationException)

3.2 CLI
- `ros2 run tf2_tools view_frames` → PDF olarak tf ağacı
- `ros2 run tf2_ros tf2_echo base_link camera_frame` → gerçek zamanlı dönüşüm
- `ros2 run tf2_ros static_transform_publisher x y z yaw pitch roll frame_id child_frame_id`

3.3 Genel Tavsiye
- StaticTransformBroadcaster vs TransformBroadcaster: ne zaman hangisi?
- lookup_transform hataları nasıl yorumlanır?
- Karar tablosu

---

Yazım kuralları:
- Türkçe, teknik terimler ilk geçişte (İngilizce) şeklinde
- Her ana kavram için `> **Gerçek hayat örneği:**` bloğu
- Teorik ağırlık, cookbook değil
- API fonksiyonları parametre tablosuyla gösterilir
- CLI örneklerinde beklenen çıktı gösterilir
- "Genel Tavsiye" bölümünde karar tablosu bulunur

Çıktıyı `markdowns/introduction-to-robotic-system-with-ros2.md` dosyasına ekle (mevcut içeriğin sonuna yeni bölüm olarak).

**Progress takibi:** İçeriği yazdıktan sonra `markdowns/progress.md` dosyasını aç, WP6 satırındaki `⬜ Bekliyor`'u `✅ Tamamlandı` ile değiştir.
```

---

## Doğrulama

Her iş paketi tamamlandıktan sonra:
1. Her ana kavramda `> **Gerçek hayat örneği:**` bloğu var mı?
2. CLI örneklerinde çıktı gösterilmiş mi?
3. API fonksiyonları için parametre tablosu var mı?
4. "Genel Tavsiye" bölümünde karar tablosu var mı?
