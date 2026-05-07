import board
import adafruit_dht



class DHT:
    _sensor = None
    last_error = None
    
    def __init__(self, board_num):
         self._sensor = adafruit_dht.DHT22(board_num)
        
    def read(self):
        reading = None
        try:
            reading = Reading(self._sensor.temperature, self._sensor.humidity)
        except Exception as error:
            last_error = error
        return reading


class Reading:
    temperature = -1
    humidity = -1
        
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
    
    def isInvalid(self):
        return self.temperature == None or self.humidity == None
    
    def __str__(self):
        if self.isInvalid():
            return "Invalid reading."
        return f"Temperature: {self.temperature:.2f} C, Humidity: {self.humidity:.2f}"
