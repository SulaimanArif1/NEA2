import socket
from Config import *

class Network:
    def __init__(self, server, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.id = self.connect()
        self.pos = [[(320, 540), (480, 540), (640, 540), (800, 540), (960, 540)] ,[(320, 156), (480, 156), (640, 156), (800, 156), (960, 156)]]

    
    def connect(self):
        try:
            self.client.connect(self.addr)
            print("Connected")
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def retpos(self,):
        return self.pos

