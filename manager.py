from sensors import *


class MANAGER:
    def __init__(self):
        self.sensor_list = []

    def add_sensor(self, sensor):
        self.sensor_list.append(sensor)
        print(f"[BİLGİ] '{sensor.name}' sisteme başarıyla eklendi.")

    def find_sensor(self, sensor_id):
        for sensor in self.sensor_list:
            if sensor.id == sensor_id: 
                return sensor
        return None

    def remove_sensor(self, sensor_id):
        sensor_to_remove = self.find_sensor(sensor_id)
        if sensor_to_remove is not None:
            self.sensor_list.remove(sensor_to_remove)
            print(f"Sensör (ID: {sensor_id}) başarıyla silindi.")
        else: 
            print("[UYARI] Böyle bir sensör bulunamadı!")

    def list_sensors(self):
        if not self.sensor_list:
            print("Sistemde henüz kayıtlı sensör yok.")
            return

        print("\n--- KAYITLI SENSÖRLER ---")
        for sensor in self.sensor_list:
            print(f"ID: {sensor.id} | İsim: {sensor.name}|birimi:{sensor.unit}|fiyat:{sensor.price}")
        print("-------------------------")



