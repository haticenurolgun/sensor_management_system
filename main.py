from sensors import *
from manager import *


admin = MANAGER()

def create_sensor():

    secim=input("eklemek istediğiniz sensör çeşidini seçin: 1-sıcaklık 2-nem 3-basınç 4-mesafe\n")
    

    isim=input("sensör ismini/modelini girin:")

    fiyat = float(input("Sensörün fiyatını girin:"))

    min_limit = float(input("Sensörün alabileceği minimum değeri girin:"))
    max_limit = float(input("Sensörün alabileceği maksimum değeri girin:"))
    
    if secim == '1': return TemperatureSensor(isim, fiyat, min_limit, max_limit)

    elif secim == '2': return HumiditySensor(isim, fiyat, min_limit, max_limit)

    elif secim == '3': return PressureSensor(isim, fiyat, min_limit, max_limit)

    else : return DistanceSensor(isim, fiyat, min_limit, max_limit)


def start():
    while True:
        print("\n=== SENSÖR YÖNETİM SİSTEMİ ===")
        print("1. Yeni Sensör Ekle")
        print("2. Sensörleri Listele")
        print("3. Sensör Sil")
        print("0. Çıkış")
        
        secim = input("İşlem seçiniz:\n")

        
        if secim == '1':
            yeni_sensor=create_sensor()
            admin.add_sensor(yeni_sensor)

        elif secim == '2':
            admin.list_sensors()


        elif secim == '3':
            sensor_id= int(input("Silmek istediğiniz sensör id'sini girin:\n"))
            admin.remove_sensor(sensor_id)
            
        elif secim == '0':
            print("Sistemden çıkılıyor...")
            break 
        else:
            print("Hatalı seçim yaptınız!")

if __name__ == "__main__":
    start() 