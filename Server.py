import time
import socket
import board
import DHT
import json
from Events import Event
import threading


HOST = '0.0.0.0'
PORT = 5002
EXIT_INSTRUCTION = "exit"


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
    print(f"[{time.time()}] Starting server @ {socket.gethostname()}")
    s.bind((HOST, PORT))
    s.listen()
    print(f"[{time.time()}] Server listening on {PORT}...")
    while True:
        print(f"{time.time()} Checking for new connection...")
        connected_socket, address = s.accept()
        try:
            handle_connection(connected_socket, address)
        except Exception as e:
            print(f"[{time.time()}] Error occurred while connected to {address}, closing connection.\n{e}")
            connected_socket.close()
    s.close()
    print(f"{time.time()} Server closing")

def handle_connection(connected_socket, address):
    print(f"{time.time()} Connected to {address}")
    while True:
        #print(f"[{time.time()}] initiate conversation")
        connected_socket.send(b'1')
        decoded = decode_message(connected_socket, address)
        if decoded == "exit" or decoded == "":
            break
        #print(f"[{time.time()}] handle message")
        handle_message(decoded)
    print(f"[{time.time()}] Connection with {address} has ended")
    connected_socket.close()

def decode_message(connected_socket, address):
    print(f"[{time.time()}] decode message")
    data = connected_socket.recv(1024)
    if not data:
        return ""
    decoded = data.decode()
    print(f"[{time.time()}] Received Instruction Data: {decoded}")
    return decoded

def handle_message(decoded_message):
    print(f"[{time.time()}] handle message")
    new_event = None 
    try:
        new_event = parse_message(decoded_message)
    except:
        print("Error parsing message")
        return
    if new_event == False:
        return
    print("new event")
    events.append(new_event)

def parse_message(decoded_message):
    print(f"[{time.time()}] parse message")
    decoded_message = json.loads(decoded_message)["instruction"]
    return Event(decoded_message[0], decoded_message[1], decoded_message[2])


def process_sensor():
    print("Starting sensor")
    sensor = DHT.DHT(board.D27)
    #events.append(Event("True", "%r"))
    while True:
        time.sleep(1)
        reading = sensor.read()
        if reading == None:
            continue
        for event in events:
            print(event.evaluate(reading))
        

                    
main()
