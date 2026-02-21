class SENSOR :

    id_counter= 0

    def __init__(self,name,unit,price):

        SENSOR.id_counter+=1

        self.name=name
        self.unit=unit
        self.price=price
        self.id= SENSOR.id_counter
        

        self.readings= []

        self.is_active = True
        

    def add_reading(self, value):

        if not self.is_active:
            return
        
        
        self.readings.append(value)

        
    def average(self):

        if not self.readings:
            return None
        else:
            return sum(self.readings)/len(self.readings)


    def deactivate(self):
        self.is_active = False


    def activate(self):
        self.is_active = True


    # def display_info(self):

    #     avg = self.average()

    #     print(f"Sensor name:{self.name} \nSensor unit:{self.unit} \n Sensor price:{self.price}\nSensor id: {self.id}")
    #     status = "ACTIVE" if self.is_active else "PASSIVE"
    #     print(f"STATUS: {status}")


    #     print("Number of readings:", len(self.readings))

    #     if avg is None:
    #         print("No measurements yet")
    #     else:
    #         print("Average:", avg)
    

class SensorLimits(SENSOR):

    def __init__(self, name, unit, price,min_limit, max_limit):
        super().__init__(name, unit, price)
        self.min_limit = min_limit
        self.max_limit = max_limit
        

    def add_reading(self, value):

        if value < self.min_limit or value > self.max_limit:
            print("Value out of allowed range!")
            return

        super().add_reading(value)


class TemperatureSensor(SensorLimits):

    def __init__(self, name, price, min_temp, max_temp):
        super().__init__(name, "C", price,min_temp, max_temp)

        


class HumiditySensor(SensorLimits):

    def __init__(self, name, price, min_hum, max_hum):
        super().__init__(name, "%", price, min_hum, max_hum)
        
        


class PressureSensor(SensorLimits):

    def __init__(self, name, price, min_pressure, max_pressure):
        super().__init__(name, "Pa", price, min_pressure, max_pressure)
        
        
class DistanceSensor(SensorLimits):

    def __init__(self, name, price, min_distance, max_distance):
        super().__init__(name, "cm", price,min_distance, max_distance)