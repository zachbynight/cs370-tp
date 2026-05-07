import socket
import time
import json
import sys


SERVER_IP = ""
PORT = 5002


EXIT_INSTRUCTION = "exit"


def main():
    SERVER_IP = sys.argv[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, PORT))
    print("Connected")
    while True:
        print(f"[{time.time()}] check if server closed")
        if s.recv(1024).decode == EXIT_INSTRUCTION:
            print(f"[{time.time()}] Server has closed")
        cont = handle_input(s, input())
        if not cont:
            break
    print(f"[{time.time()}] Closing connection")
    s.close()
    print("Exiting program")


INPUT_PASS = 0
INPUT_EXIT = 1
INPUT_INSTRUCTION = 2

def handle_input(s, input_str):
    input_type = determine_input_type(input_str)
    if input_type == INPUT_PASS:
        return True
    if input_type == INPUT_EXIT:
        send_instruction(s, EXIT_INSTRUCTION)
        return False
    new_instruction = Instruction.parse(input_str)
    send_instruction(s, str(new_instruction))
    return True

def determine_input_type(input_str):
    input_str = input_str.strip()
    if input_str == EXIT_INSTRUCTION:
        return INPUT_EXIT
    if Instruction.is_parseable(input_str):
        return INPUT_INSTRUCTION
    return INPUT_PASS

def send_instruction(s, message_string):
    try:
        print(f"[{time.time()}] try sending")
        s.sendall(message_string.encode())
        print(f"[{time.time()}] Sent {message_string}")
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
    
    def as_json(self):
        return {
            "instruction": 
                [
                    self.expression,
                    self.good_message,
                    self.bad_message
                ]
        }
    
    def __str__(self):
        return json.dumps(self.as_json())
        
        
main()
