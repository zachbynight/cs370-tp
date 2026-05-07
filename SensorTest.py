from DHT import *
import board


def main():
    sensor = DHT(board.D27)
    while True:
        print(sensor._sensor.temperature)
        print(sensor._sensor.humidity)
    return
    while True:
        reading = sensor.read()
        if reading == None:
            print(f"Error: error reading sensor. {sensor.last_error}")
            continue
        if reading.isInvalid():
            print(f"Error: sensor not read correctly. {sensor.last_error}")
            continue
        print(reading)


main()
