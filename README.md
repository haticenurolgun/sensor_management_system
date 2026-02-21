
Bu çalışmada aşağıdaki OOP kavramlarını gerçek bir senaryo üzerinde uygulamayı hedefledim:

Inheritance (Kalıtım): * Tüm sensörlerin ortak özelliklerini (isim, fiyat, birim) SENSOR ana sınıfında topladım.

SensorLimits sınıfı ile limit kontrolü yeteneğini ekledim.

Temperature, Humidity, Pressure ve Distance sınıfları ile özelleştirilmiş alt sınıflar oluşturdum.

Encapsulation (Kapsülleme): * Sensör verilerini (readings) ve durum bilgilerini sınıf içinde saklayarak, bu verilere sadece sınıf içindeki metotlar (add_reading, average) aracılığıyla erişilmesini sağladım.

Abstraction (Soyutlama): * Kullanıcının sensörün içindeki karmaşık hesaplamaları (ortalama alma, limit kontrolü) bilmesine gerek kalmadan, sadece basit metotları çağırarak sonuç almasını sağladım.

Polymorphism (Çok Biçimlilik): * Farklı sensör tiplerinin (TemperatureSensor, DistanceSensor vb.) aynı metot isimlerini (display_info) kullanarak kendilerine has çıktı vermelerini sağladım.

🏗️ Mimari Yapı (Separation of Concerns)
Proje, sorumlulukların net ayrılması için üç ana modüle bölünmüştür:

sensors.py (Domain Logic): Sensörlerin "şablonlarını" barındırır. Veri doğrulama ve matematiksel işlemler burada gerçekleşir.

manager.py (Data Management): Sensör nesnelerini bir arada tutan, arama ve silme operasyonlarını yöneten "Yönetici" sınıfıdır.

main.py (User Interface): Kullanıcı etkileşimini ve nesne yaratım süreçlerini yöneten orkestra şefidir.
