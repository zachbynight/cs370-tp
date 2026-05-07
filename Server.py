import time
import socket
import board
import DHT
from Events import Event
import threading


HOST = '0.0.0.0'
PORT = 5000


events = []


def main():
    try:
        networking_thread = threading.Thread(target=process_network_requests, args=(), kwargs={})
        networking_thread.start()
        sensor_thread = threading.Thread(target=process_sensor, args=(), kwargs={})
        sensor_thread.start()
        networking_thread.join()
        sensor_thread.join()
    except:
        print("Error occured")


def process_network_requests():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Starting server @ {socket.gethostname()}")
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {PORT}...")
    while True:
        if input() == "exit":
            break
        connected_socket, address = s.accept()
        try:
            handle_connection(connected_socket, address)
        except Exception as e:
            print(f"Error occurred while connected to {address}: {e}")
    s.close()
    print("Server closing")

def handle_connection(connected_socket, address):
    print(f"Connected to {address}")
    while True:
        connected_socket.send(b'1')
        decoded = handle_message(connected_socket, address)
        if decoded == "exit":
            break
        new_event = parse_message(decoded)
        if new_event == None:
            continue
        events.append(new_event)
    connected_socket.close()

def handle_message(connected_socket, address):
    data = connected_socket.recv(1024)
    if not data:
        return ""
    decoded = data.decode()
    print(f"Received Instruction Data: {decoded}")
    return decoded

def parse_message(message):
    items = message.split()
    if len(items) != 2 and len(items) != 3:
        return False
    if len(items) == 2:
        items.append("")
    return Event(items[0], items[1], items[2])


def process_sensor():
    print("Starting sensor")
    sensor = DHT.DHT(board.D27)
    events.append(Event("True", "%r"))
    while True:
        time.sleep(1)
        reading = sensor.read()
        if reading == None:
            continue
        for event in events:
            print(event.evaluate(reading))
        

                    
main()
