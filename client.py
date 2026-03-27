from server import address as server_address
from socket import *


def start():
    client_socket = socket()
    client_socket.connect(server_address())
    client_socket.sendall(bytes("abcd", "utf-8"))
    client_socket.sendall(b"\n")
    client_socket.close()