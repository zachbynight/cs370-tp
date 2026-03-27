def main():
  print(get_reading())


def get_reading():
    return Reading(10, 50)


class Reading:
    _humidity = -1
    _temperature = -1

    def __init__(self, h, t):
        self._humidity = h
        self._temperature = t

    def humidity(self):
        return self._humidity

    def temperature(self):
        return self._temperature
        
    def __repr__(self):
        return f"Reading({self._humidity}, {self._temperature})"
    
    def __str__(self):
        return f"{self._humidity}%, {self._temperature}° C"


main()