# Plan: communication.md Tamamlama

## Bağlam

`markdowns/core-features/communication.md` dosyası ROS2 haberleşme konseptlerini anlatan bir öğretim dokümanı. Teori bölümü kısmen yazılmış ancak birçok kritik bölüm boş veya TODO durumunda. Dosyanın `theory.md` dokümanının devamı niteliğinde olduğu görülüyor — aynı didaktik tonu ve günlük hayat analojisi yaklaşımını korumalı.

---

## Yapılacaklar

### 1. Yapısal düzeltmeler (küçük ama önemli)

- **İçindekiler** → Markdown anchor linkleriyle tıklanabilir hale getir  
  Örn: `[2.1 Topic](#21-topic)`

- **Action Service örneği tutarsızlığı** → "Silme işlemi" analogisini daha robotik/yakın bir örnekle değiştir (ör. robota "şu rafa git ve nesneyi al" komutu, yolculuk boyunca konum bildirimi, sonunda "tamamlandı").

---

### 2. Bölüm 1 — Giriş

Tek cümleyi kaldır, şunu yaz:
- Bu dosyanın `theory.md`'den sonra geldiğini ve ROS2'nin haberleşme altyapısını uygulama düzeyinde ele aldığını belirt
- Okuyucunun bu dosyadan ne öğreneceğini (teori + Python API + CLI araçları) kısaca aktar
- Ton: öğretici ve davet edici, teknik jargonsuz

---

### 3. Bölüm 2.4 — Özel Mesaj Arayüzleri

Sadece sezgisel anlatım, teknik detay yok, günlük hayat analogisi olsun.

İçerik:
- İletişimdeki "ortak dil" metaforu: iki taraf aynı mesaj formatını konuşmalı
- Standart arayüzler (std_msgs, geometry_msgs vb.) → hazır kelime dağarcığı gibi; başkalarıyla uyumlu, tercih edilmeli
- Özel arayüzler (.msg, .srv, .action) → standart seçenekler yetersiz kaldığında kendin tanımlıyorsun; özel jargon gibi
- Gerçek hayat analogisi: uluslararası kargo formları — standart format var, ama özel sektörler kendi alanlarını ekliyor

---

### 4. Bölüm 3 — Kullanım girişi

TODO yorumunu gerçek bir paragrafla değiştir: bu bölümün Python API ve CLI araçlarını örneklerle göstereceğini belirt.

---

### 5. Bölüm 3.1 — API (Python)

Her alt bölüm için **açıklamalı tam node** — copy-paste çalışır, her satır ne yapıyor prose veya inline yorum olarak açıklanıyor.

#### 3.1.1 Topic
- Publisher node: `std_msgs/String` mesajı yayımlıyor
- Subscriber node: aynı topic'i dinleyip callback'te mesajı basan

#### 3.1.2 Service
- Server node: istek alıp yanıt döndüren (ör. iki sayı toplama — `example_interfaces/AddTwoInts`)
- Client node: servise istek gönderip sonucu bekleyen

#### 3.1.3 Action Service
- Action server node: goal alıp feedback göndererek ilerleyen, sonunda result döndüren
- Action client node: goal gönderip feedback'i izleyen, result'ı bekleyen
- `example_interfaces/action/Fibonacci` kullanılabilir

Her node için: import → sınıf → `__init__` → callback/handler → `main()` yapısı korunacak.

---

### 6. Bölüm 3.2 — CLI

`ros2 topic`, `ros2 service`, `ros2 action` komutlarının temel kullanımı:

- `ros2 topic list / echo / pub`
- `ros2 service list / call`
- `ros2 action list / send_goal`

Her komut için kısa açıklama + örnek çıktı.

---

### 7. Bölüm 3.3 — Genel Tavsiye

"Hangi iletişim türünü seç?" sorusuna pratik cevap. Karşılaştırma tablosu burada yer alır:

| Özellik          | Topic | Service | Action |
|------------------|-------|---------|--------|
| Yanıt garantisi  | Hayır | Evet    | Evet   |
| Asenkron         | Evet  | Hayır   | Evet   |
| Süreç takibi     | Hayır | Hayır   | Evet   |
| Çok alıcı        | Evet  | Hayır   | Hayır  |

Tablonun altına 2-3 cümlelik pratik özet.

---

## Kritik dosya

- `markdowns/core-features/communication.md` — tek dosya değiştiriliyor

## Doğrulama

- Markdown render'ında İçindekiler linkleri çalışıyor mu?
- Kod blokları Python syntax highlight alıyor mu? (` ```python `)
- Tüm TODO yorumları kaldırıldı mı?
- Anolojiler birbirleriyle tutarlı mı (Action Service örneği eskisiyle çelişmiyor mu)?
