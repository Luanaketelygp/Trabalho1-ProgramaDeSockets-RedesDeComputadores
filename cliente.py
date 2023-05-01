import socket
from random import randint
import time

HOST = '127.0.0.1'
PORT = 5000
MIN_LENGTH = 1
MAX_LENGTH = 999999999999999999999999999999
RANDOM_NUMBER = str(randint(MIN_LENGTH, MAX_LENGTH))
TIME_EXECUTE = 10

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(str.encode(RANDOM_NUMBER))
    data = s.recv(1024)
    print(data.decode(), ': FIM')

    time.sleep(TIME_EXECUTE)