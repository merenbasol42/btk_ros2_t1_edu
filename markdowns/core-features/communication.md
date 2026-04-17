# İçindekiler

<!-- TODO: burada başlıklar tıklanıp ulaşılabilir olmalı -->

# 1. Giriş

Bu yazı ROS2'de haberleşme özelliğinin ne olduğunu anlatır.

<!-- TODO: buraya bir giriş yazısı yaz bağlam açısından bu dosya neyi ifade ediyor gibisinden -->

# 2. Teori

ROS'ta iletişim **kanallar** üzerinden yapılır. Bu kanallar 3 tiptir: **topic**, **service** ve **action service**.

Her kanalın uyması gereken iki temel kural vardır:

1. Her kanalın benzersiz bir ismi olmalı
2. Her kanalın bir mesaj tipi olmalı

Bu iki kural, tüm iletişim türleri için geçerlidir.

## 2.1 Topic

Topic kanalında iki tür iletişimci vardır: **yayımcı (publisher)** ve **abone (subscriber)**.

Yayımcı kanala veri yollar, abone ise o kanalı dinleyip gelen mesajlardan haberdar olur. Abone olurken bir "callback" fonksiyonu verirsiniz; ROS da mesaj geldiğinde bu fonksiyonu çağırarak size veriyi teslim eder.

> **Gerçek hayat örneği:** Radyo. Bir frekansı ayarlarsınız — diyelim 98.1 — ve artık o frekanstaki yayınları dinlersiniz. Bir frekansa birden fazla dinleyici olabileceği gibi, birden fazla yayıncı da olabilir. Topic kanalı da tıpkı bunun gibidir.

## 2.2 Service

Servisler klasik **server–client** mantığıyla çalışır. Sunucu bir servis kanalı açar ve bir callback fonksiyon tanımlar. İstemci, bu servise bir istek gönderir ve karşılığında mutlaka bir yanıt alır.

Servisler, "mesaj gönder, cevap al" tarzı iletişimlerde kullanılır. Topic ile bu tür bir yanıt garantisini elde edemezsiniz, ama service size bunu sağlar.

> **Gerçek hayat örneği:** Restoran siparişi.
> 1. Müşteri (Client) garsona sipariş verir: *"Bir pizza istiyorum."*
> 2. Garson (Server) isteği alır, mutfağa iletir ve sonucu bekler.
> 3. Pizza hazır olduğunda garson müşteriye teslim eder: *"Buyurun, pizzanız hazır!"*
> 4. Müşteri (Client) yanıtı aldıktan sonra işlem tamamlanır.

## 2.3 Action Service

Aksiyon servisleri, iki servis + bir topic birleşimi gibidir. Uzun süren işlemlerde, ara ara bilgi almak veya süreci takip etmek istediğimizde kullanılır.

Örneğin, robotunuza "şu konuma git ve dengede kal" diyorsunuz. Robot dengede kalmaya çalışırken siz de "şu anda hız sınırını aşıyor mu, ne kadar kaldı" gibi bilgileri almak istiyorsunuz. İşte burada action servisleri devreye giriyor.

> **Gerçek hayat örneği:** Bir "silme işlemi" yapıyorsunuz.
> 1. İsteği gönderiyorsunuz
> 2. Sistem isteği kabul ediyor
> 3. Sistem size *"%30 tamamlandı, %70 tamamlandı…"* diye ilerleme bildiriyor
> 4. En sonunda *"tamam, işlem bitti"* diyerek sonucu döndürüyor

Yani hem süreç takibi yapabiliyor, hem de sonunda sonucu alabiliyorsunuz.

## 2.4 Özel Mesaj Arayüzleri

<!-- TODO: Burada mesaj arayüzlerinin anlatımı ve özel mesaj arayüzlerinin bi anlatımı olsun günlük hayattan örneklerle sadece teorik ve basit olsun kullanıma dair api cli hiç bir şey gösterilmesin -->

# 3. Kullanım

Burada ROS2'nin haberleşme için sunduğu API ve CLI araçlarının kullanımından örneklerle bahsedeceğiz.

<!-- TODO: buraya bir yazı lazım yukardakini çok beğenmedim  -->

## 3.1. API

<!-- TODO: burada API kullanımı python üzerinden anlatılacak -->

### 3.1.1. Topic

### 3.1.2. Service

### 3.1.3. Action Service

### 3.1.4. Custom Interfaces


## 3.2 CLI


## 3.3 Genel Tavsiye

