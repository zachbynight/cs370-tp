def main():
    a = get_reading()
    print(a.humidity())


def get_reading():
    return Reading(10, 50)


class Reading:
    _humidity = -1
    _temperature = -1

    def __new__(self, h, t):
        self._humidity = h
        self._temperature = t
        return self

    def humidity(self):
        return self._humidity

    def temperature(self):
        return self._temperature
    
    def a_func(self):
        return f"{self._humidity}%, {self._temperature}° C"


main()