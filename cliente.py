import socket
from random import randint
import time

HOST = '127.0.0.1'
PORT = 5000
MIN_DIGITS = 1
MAX_DIGITS = 30
TIME_EXECUTE = 10

def random_number_with_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
                   
while True:
    RANDOM_NUMBER = str(random_number_with_digits(randint(MIN_DIGITS, MAX_DIGITS)))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(str.encode(RANDOM_NUMBER))
    data = s.recv(1024)
    print(data.decode(), ': FIM')

    time.sleep(TIME_EXECUTE)
