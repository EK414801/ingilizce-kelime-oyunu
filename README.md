İngilizce Kelime Oyunu

Bu proje, kullanıcıların İngilizce kelime dağarcığını eğlenceli ve etkileşimli bir şekilde geliştirmesi için tasarlanmış, ses tanıma özellikli bir terminal oyunudur. Yazılım, yetkisiz kullanımı önlemek amacıyla bir Lisans Dosyası doğrulama sistemi ile çalışmaktadır.

🌟 Özellikler

Sesli Etkileşim: Cevaplar klavyeden yazılmaz, mikrofon aracılığıyla sesli olarak söylenir.

Zorluk Seviyeleri:

Kolay: Doğru cevap +5 puan.

Orta: Doğru cevap +10 puan.

Zor: Doğru cevap +20 puan.

Can Sistemi: Kullanıcı 3 can ile başlar. Yanlış cevaplarda 1 can eksilir, 0 canda oyun biter.

Akıllı Gelişim Yardımcısı: Oyun sonunda devreye giren bu modül, kullanıcının eksiklerini analiz ederek İngilizcesini geliştirmesi için kişiselleştirilmiş tavsiyeler sunar.

🚀 Başlangıç

Yazılımı kullanmaya başlamak için geçerli bir lisans dosyasına sahip olmanız ve gerekli kütüphaneleri kurmanız gerekmektedir.

Gereksinimler

Python 3.8+

İnternet Bağlantısı (Ses tanıma motoru ve lisans kontrolü için)

Mikrofon

Geçerli bir lisans dosyası (license.py)

Kurulum

Dosyaları İndirin: Projeyi yerel dizine klonlayın.

Bağımlılıkları Yükleyin:
Ses tanıma ve mikrofon erişimi için gerekli kütüphaneleri kurun:

pip install -r requirements.txt


(Not: SpeechRecognition, PyAudio ve gTTS kütüphanelerini içerir.)

Lisans Dosyasını Yerleştirin: Satın aldığınız license.lic dosyasını ana dizine kopyalayın.

🎮 Oyunun İşleyişi

Giriş: Program açıldığında lisans dosyanız doğrulanır.

Seçim: "Kolay", "Orta" veya "Zor" modlarından birini seçersiniz.

Oyun: Ekranda bir İngilizce kelime belirir. Bu kelimenin Türkçe karşılığını sesli olarak söylemeniz istenir.

Puanlama: Doğru cevapta seçtiğiniz moda göre puan kazanırsınız. Yanlış cevapta 3 canınızdan biri eksilir.

Final: Oyun bittiğinde sistem size "Yardımcıya girmek ister misiniz?" diye sorar:

Evet: Sistem size özel sorular sorarak İngilizcenizi nasıl geliştirebileceğinize dair bir yol haritası çıkarır.

Hayır: Program başarıyla sonlandırılır.

🔑 Lisans Aktivasyonu

Yazılım, license.py dosyası üzerinden donanım kimliği (HWID) kontrolü yapar. Lisans bulunamazsa oyun başlatılmaz.

🛠️ Kullanım

Uygulamayı başlatmak için terminale şu komutu yazın:

python main.py


❓ Destek ve Lisans Satın Alma

Yeni bir lisans satın almak veya destek talebi oluşturmak için:

E-posta:ek.bagirci48@gmail.com

© 2026 Tüm hakları saklıdır.
