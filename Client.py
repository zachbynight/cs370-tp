import socket
import time
import json
import sys


SERVER_IP = ""
PORT = 5000


def main():
    SERVER_IP = sys.argv[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, PORT))
    if s.recv(1) != b'1':
        print("Connected could not be started")
        return
    print("Connected")
    while True:
        input_str = input()
        input_type = determine_input_type(input_str)
        if input_type == INPUT_PASS:
            print("Invalid input")
            continue
        if input_type == INPUT_EXIT:
            s.sendall("exit".encode())
            print("Closing connection")
            s.close()
            break
        new_instruction = Instruction.parse(input_str)
        send_instruction(s, str(new_instruction))
    print("Exiting program")


INPUT_PASS = 0
INPUT_EXIT = 1
INPUT_INSTRUCTION = 2

def determine_input_type(input_str):
    input_str = input_str.strip()
    if input_str == "exit":
        return INPUT_EXIT
    if Instruction.is_parseable(input_str):
        return INPUT_INSTRUCTION
    return INPUT_PASS

def send_instruction(s, message_string):
    try:
        # print("check if server closed")
        if s.recv(1024).decode == "exit":
            s.close()
            # print("connected closed")
            return
        # print("try sending")
        s.sendall(message_string.encode())
        # print(f"Sent {message_string}")
    except Exception as e:
        print(f"ERROR: {e}")


class Instruction:
    expression = ""
    good_message = ""
    bad_message = ""
    
    @staticmethod
    def is_parseable(text):
        items = text.split()
        return len(items) == 2 or len(items) == 3
    
    @staticmethod
    def parse(text):
        items = text.split()
        if not Instruction.is_parseable(text):
            return None
        if len(items) == 2:
            items.append("")
        return Instruction(items[0], items[1], items[2])
    
    def __init__(self, expression, good_message, bad_message):
        self.expression = expression
        self.good_message = good_message
        self.bad_message = bad_message
    
    def __str__(self):
        text = {
            0: self.expression,
            1: self.good_message,
            2: self.bad_message
        }
        return json.dumps(text)
        
        
main()
