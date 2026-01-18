import speech_recognition as sr
import random
import time
from lisansd import lisans

print("=== İngilizce Kelime Oyunu sürümü 3.4 ===")

print("lütfen bekleyin lisans doğrulaması yapılıyor🤖...")
if lisans == "vx3@PL&kdnCd#-oGWE+Uuu56!ab6Ba*LpcIUP=0j$p/=?7pBr0ZF6qbn6Zw7K?OFlMh0VZeAxh&0JCo7HNV3CBoB?iQ6*6GL+VUyLpr?NSt*1bz&=-904L2nPWpE=YpI+yPASbXqL-pT&r?RnEL90QZ7uS1UqtX/iMvpOOi7#Z4#FV-!#APMipCQpjaY5lwbN6ygbTi89Whxx#XOgAUEqtOheauuus!X!EiBLb*K3Cq=G$NOMWD?aKY-hq9e?RRa17newlr*o*UUG!1r+A8nP7MGe5g6gqsx52Cp!ZWEQH/IxEjNOUFdTnKKSG=-N8s-AGq2QWKNe1!=TfkGlJEO$3GqTgEG-C/tIKpHHaOIg5cghS4RVZ*72yX0RTrC0X*cM8SRkikn*Hc+Vx$jDWyHtwcEayxHFFbO=&Kri+&T@kMAKwUv0VzEl&tcW0r7sp-daQk-SZIarPdit5?p5!Spu7RiV3YFw7ncOG6l*+qqq?fpEACy2CWy4dLrF*f?P7?n1j0Un87A/s&dCyAa#4ptRoPdK/7wpHOMCnwgCds-@Jior2ngd&i#0P=6HhV=IbI2RrgZtrl!$z4-p$LAFB/dp!l9z/hLdFbFiM$WdDok$ZPq3oiT/Nh?hM/cat@z$DiuB*NQjNQATC@!$u&n=1u=iSN&QC*ykTK/$JE-HqGA*EEAW!7OdC$TVB1F-KFLQtdYArRP?EwF$AOFO$WNJMBMQGTHS7XzTz4ytvvGWRsIWkMDXHi+VME01fBA!Pp+KY0fFRvoQ+nI1TL*SLj6H?sHofyz-hJcY5KeCnVk+3T$U07uhZyVsrpGuWS/t@2fSbs03R$KlzNbb3jfBY3tSrpXSaTk?g0HlP9U47JEO@*DdJh1l/*L&HSX!d6VCshv3nNS/0nc8F#+iJXUuazb*c5VLZd5JbfEIHkCne?pXvvDbMhjWZk8SDRDHYUacn8kiVXC*IbHE36uG-KEZ4TLDheb9T0e2?1acfabQ8Wku#wB":
    print("lütfen bekleyin program başlatılıyor🤖...")
    izin = True
else:
    print("❌ Lisans doğrulaması başarısız! Program sonlandırılıyor. ❌")
    izin = False
    
# Seviyeye göre kelime listeleri
seviyeye_gore_kelimeler = {
    "kolay": ["cat", "dog", "apple", "milk", "sun", "open", "book", "tree", "car", "house"],
    "orta": ["banana", "school", "friend", "window", "yellow", "eat", "computer", "garden", "family", "music"],
    "zor": ["technology", "university", "information", "pronunciation", "imagination", "because", "development", "environment", "responsibility", "architecture"]
}

# Kelimelerin Türkçe karşılıkları (Cevapları kontrol etmek için)
turkce_karsiliklar = {
    "cat": "kedi", "dog": "köpek", "apple": "elma", "milk": "süt", "sun": "güneş", "open": "açmak", "book": "kitap", "tree": "ağaç", "car": "araba", "house": "ev",
    "banana": "muz", "school": "okul", "friend": "arkadaş", "window": "pencere", "yellow": "sarı", "eat": "yemek", "computer": "bilgisayar", "garden": "bahçe", "family": "aile", "music": "müzik",
    "technology": "teknoloji", "university": "üniversite", "information": "bilgi", 
    "pronunciation": "telaffuz", "imagination": "hayal gücü", "because": "çünkü", "development": "gelişim", "environment": "çevre", "responsibility": "sorumluluk", "architecture": "mimari"
}

def start_game():
    can = 3
    puan = 0
    
    print("=== İngilizce Kelime Oyununa Hoş Geldiniz! 🚀 🎮 ===")
    
    recognizer = sr.Recognizer()

    # Ana oyun döngüsü
    while can > 0:
        # Seviye seçimi döngünün içine alındı, böylece her turda veya hata payında seçilebilir
        while True:
            seviye = input("\nLütfen bir seviye seçin (kolay, orta, zor)😊 (Çıkmak için 'q'): ").lower()
            if seviye == 'q':
                can = 0
                break
            if seviye in seviyeye_gore_kelimeler:
                break
            print("Geçersiz seviye! Lütfen tekrar deneyin😒.")
        
        if can <= 0: break

        # Seçilen seviyeden bir kelime sor
        secilen_kelime = random.choice(seviyeye_gore_kelimeler[seviye])
        dogru_cevap = turkce_karsiliklar[secilen_kelime]
        
        print(f"\nSoru: '{secilen_kelime}' kelimesinin Türkçe karşılığı nedir🤔")
        print(f"❤️ Mevcut Can: {can} | 🏆 Mevcut Puan: {puan}")
        
        with sr.Microphone() as source:
            print("🎤Konuşmaya başlayın😃... (Dinleniyor)")
            recognizer.adjust_for_ambient_noise(source)
            
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio, language="tr-TR").lower()
                print(f"🗣️Söylediğiniz: {text}")

                if text == dogru_cevap:
                    print("✅Tebrikler! Doğru bildiniz 😊 😍")
                    if seviye == "kolay":
                        puan += 5
                    elif seviye == "orta":
                        puan += 10
                    elif seviye == "zor":
                        puan += 20
                else:
                    can -= 1
                    print(f"❌Maalesef yanlış 😒 😒 Doğru cevap: {dogru_cevap}")

            except sr.UnknownValueError:
                print("❓ HATA: Ses anlaşılamadı! 🫨 ⚠️")
                print("🤖 Lütfen daha net konuşmaya çalışın.")
            except sr.WaitTimeoutError:
                print("⏳ HATA: Dinleme süresi doldu! 💤")
            except sr.RequestError:
                print("🌐Servise ulaşılamıyor😭, internet bağlantınızı kontrol edin.🔌 🚫")
                break
            except Exception as e:
                print(f"😭Bir hata oluştu🤖💥🔧: {e}")
                break

    # Oyun bittiğinde gösterilecek ekran
    print("\n" + "═"*30)
    print(f"💀 OYUN BİTTİ! 💀")
    print(f"📊 Final Puanınız: {puan}")
    if puan > 200:
        print("🌟 Harika bir iş çıkardın!")
    else:
        print("🏗️ Biraz daha pratik yaparak gelişebilirsin!")
    print("═"*30)
    print("puan hesaplayıcıyı açmak ister misiniz.(çok mu iyisiniz yoksa çok mu kötüsünüz öğrenmek için ve geliştirmek için öneride bulunacak) E/H")
    k=input(">>>")
    if k.lower()=="E" or "e":
        puan_hesaplayici(puan)
    elif k.lower()=="H" or "h":
        print("tekrar görüşmek üzere😊")
    else:
        print("tekrar görüşmek üzere😊")
    

def puan_hesaplayici(puan):
    print("\n=== Puan Hesaplayıcı ===")
    print("Merhaba! Lütfen bekleyin puanınız analiz ediliyor...")
    print(f"Toplam puanınız: {puan}")
    print("size bazı sorular sormalıyız...")
    k = input("ingilizce tekrar yapıyor musunuz? e/h")
    u = int(input("günde kaç sayfa kitap okuyorsunuz?"))
    print("analiz yapılıyor...")
    if puan > 50 and puan <= 100 and  k.lower() == "h" and u < 10 : # 1
        print("İngilizce seviyeniz başlangıç seviyesi.")
        print("artık ingilizce tekrarı yapmaya başlamalısınız. ingilizce hemen unutulan dildir.")
        print("çok az kitap okuyorsunuz😒📘.")
        print("günde en az 20 sayfa kitap okuyun📕.")
    elif puan > 100 and puan <= 200 and k.lower() == "e" and u >= 15 : # 2
        print("İngilizce seviyeniz orta seviye.")
        print("ingilizce tekrarlarınıza devam edin ve kelime bilginizi artırın.")
        print("günde en az 30 sayfa kitap okuyun📕.")
    elif puan > 200 and k.lower() == "e" and u >= 30: # 3
        print("İngilizce seviyeniz ileri seviye.")
        print("ingilizceniz çok iyi durumda😃😃.")
        print("mükemmel bir iş çıkardınız! İngilizce pratiğinize devam edin ve akıcılığınızı artırın📘📕.")
        print("günde en az 50 sayfa kitap okuyun ve ingilizce makaleler okuyun📕📘.")
    elif puan > 50 and puan < 100 and k.lower() == "e" and u >= 10: #1
        print("İngilizce seviyeniz başlangıç-orta seviye arası.")
        print("ingilizce tekrarlarınıza devam edin ve kelime bilginizi artırın.")
        print("günde en az 20 sayfa kitap okuyun📕.")
    elif puan > 50 and puan < 100 and k.lower() == "e" and u < 10: # 1 
        print("İngilizce seviyeniz başlangıç seviyesi.")
        print("ingilizce tekrarlarınıza devam edin ve kelime bilginizi artırın.")
        print("çok az kitap okuyorsunuz😒📘.")
        print("günde en az 15 sayfa kitap okuyun📕.")
    elif puan > 50 and puan < 100 and k.lower() == "h" and u >= 10: # 1
        print("İngilizce seviyeniz başlangıç seviyesi.")
        print("ingilizce tekrarlarına başlayın ve kelime bilginizi artırın.")
        print("günde en az 15 sayfa kitap okuyun📕.")
    elif puan > 100 and puan <= 200 and k.lower() == "e" and u <= 15 : # 2
        print("İngilizce seviyeniz orta seviye.")
        print("ingilizce tekrarlarınıza devam edin ve kelime bilginizi artırın.")
        print("çok az kitap okuyorsunuz😒📘.")
        print("günde en az 25 sayfa kitap okuyun📕.")
    elif puan > 100 and puan <= 200 and k.lower() == "h" and u >= 15 : # 2
        print("İngilizce seviyeniz başlangıç-orta seviye arası.")
        print("ingilizce tekrarlarına başlayın ve kelime bilginizi artırın.")
        print("günde en az 30 sayfa kitap okuyun📕.")
    elif puan > 100 and puan <= 200 and k.lower() == "h" and u <= 15 : # 2
        print("İngilizce seviyeniz başlangıç seviyesi.")
        print("artık ingilizce tekrarı yapmaya başlamalısınız. ingilizce hemen unutulan dildir.")
        print("çok az kitap okuyorsunuz📘😒.")
        print("günde en az 20 sayfa kitap okuyun📕.")
    elif puan > 100 and puan <= 200 and k.lower() == "e" and u <= 15 : # 2
        print("İngilizce seviyeniz orta seviye.")
        print("ingilizce tekrarlarınıza devam edin ve kelime bilginizi artırın.")
        print("çok az kitap okuyorsunuz😒📘.")
        print("günde en az 25 sayfa kitap okuyun📕.")
    elif puan > 200 and k.lower() == "e" and u <= 30: # 3
        print("İngilizce seviyeniz orta-ileri seviye arası.")
        print("ingilizce pratiğinize devam edin ve akıcılığınızı artırın.")
        print("çok az kitap okuyorsunuz😒📘.")
        print("günde en az 40 sayfa kitap okuyun ve ingilizce makaleler okuyun📕.")
    elif puan > 200 and k.lower() == "h" and u >= 30: # 3
        print("İngilizce seviyeniz orta seviye.")
        print("ingilizce tekrarlarına başlayın ve kelime bilginizi artırın.")
        print("çok az kitap okuyorsunuz😒📘.")
        print("günde en az 40 sayfa kitap okuyun ve ingilizce makaleler okuyun📕.")
    elif puan > 200 and k.lower() == "h" and u <= 30: # 3
        print("İngilizce seviyeniz başlangıç-orta seviye arası.")
        print("ingilizce tekrarlarına başlayın ve kelime bilginizi artırın.")
        print("çok az kitap okuyorsunuz😒📘.")
        print("günde en az 30 sayfa kitap okuyun ve ingilizce makaleler okuyun📕.")

    elif puan <= 50:
        print("İngilizce seviyeniz çok düşük.")
        print("acilen ingilizce tekrarlarına başlamalısınız ve kelime bilginizi artırmalısınız😭.")
        print("günde en az 15 sayfa kitap okuyun📕.")
    
    else:
        print("bazı bilgiler doğru girilmemiş lütfentekrar deneyin😒.")

    print("bizim dediklerimizi uygularsanız ingilizce de çok iyi olursunuz.")
    
    
    print("görüşmek üzere😊")
   

print("Oyun için teşekkürler! Tekrar görüşmek üzere! 👋😊")

if __name__ == "__main__":
    if izin == True:
        start_game()