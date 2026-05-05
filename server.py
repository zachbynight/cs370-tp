import time
import socket
import board
import dht
from events import Event

HOST = '0.0.0.0'
PORT = 5000


def main():
    print("Starting server")
    sensor = dht.DHT(board.D27)
    e1 = Event("True", "Humidity is %h%")
    e2 = Event("humidity>50", "Quite humid", "Not humid")
    reading = None
    while reading == None:
        reading = sensor.read()
    print(e1.evaluate(reading))
    print(e2.evaluate(reading))

def setup():
   pass

def send_data():
    try:
        temp = pid.temperature
        hum = pi.humdity 
        message = f"Temperature: {temp:.1f}F, Humidity: {hum:.1f}%"

        #connects with the server device and will send the message as a stream of bytes
        with sockets.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, PORT))
            s.sendall(message.encode())
            print(f"Sent {message}")

    except Exception as e:
        print(f"ERROR: {e}")


def old_networking():
    #This will send the message ever second
    while true:
        send_data()
        time.sleep(60)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen
        print(f"Server listening on {PORT}...")

        while True:
            conn, addr = s.accept
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    print(f"Received Sensor Data: {data.decode()}")
                    
main()
