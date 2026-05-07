import time
import socket
import board
import dht
from events import Event
import threading

HOST = '0.0.0.0'
PORT = 5000

connected = None

def main():
    try:
        networking_thread = threading.Thread(target=process_network_requests, args=(), kwargs={})
        networking_thread.start()
        print("Starting sensor")
        sensor = dht.DHT(board.D27)
    except:
        print("Error occured")

def process_network_requests():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Starting server @ {socket.gethostname()}")
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {PORT}...")
        while True:
            connected_socket, address = s.accept()
            try:
                handle_connection(connected_socket, address)
            except Exception as e:
                print(f"Error occurred while connected to {address}: {e}")

def handle_connection(connected_socket, address):
    print(f"Connected to {address}")
    while True:
        connected_socket.send(b'1')
        decoded = handle_message(connected_socket, address)
        if decoded == "exit":
            break
    connected_socket.close()

def handle_message(connected_socket, address):
    data = connected_socket.recv(1024)
    if not data:
        return ""
    decoded = data.decode()
    print(f"Received Instruction Data: {decoded}")
    return decoded




                    
main()
