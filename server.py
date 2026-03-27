from socketserver import *


PORT = 50505
ADDRESS = "127.0.0.1"


def address():
    return (ADDRESS, PORT)


def start():
    sensorServer = SensorServer((ADDRESS, PORT), RequestHandler)
    sensorServer.timeout = 10
    print("Server started")
    for i in range(3):
        print("waiting for request")
        sensorServer.handle_request()
    print(f"server received {sensorServer.num_requests} requests")
    sensorServer.server_close()


class SensorServer(UDPServer):
    num_requests = 0


class RequestHandler(BaseRequestHandler):
    def handle(self):
        print("received request")
        print(self.request.recv(1000))
        server.num_requests += 1