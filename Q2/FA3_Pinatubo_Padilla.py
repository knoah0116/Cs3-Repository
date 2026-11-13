from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class TempSensor(Sensor):
    def get_reading(self):
        return "26 deg C"
    def __str__(self):
        return "[Temperature Sensor] Reading: 24.5°C"

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH"
    def __str__(self):
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"



print("--- Lab Inventory System ---")
tempSensor=TempSensor()
phSensor=PHSensor()
print(tempSensor)
print(phSensor)
print("")
print("----------------")
