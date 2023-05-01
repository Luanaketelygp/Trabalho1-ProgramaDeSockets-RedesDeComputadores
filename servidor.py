import socket
import string
import random

def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    print ('Aguardando conexão de um cliente')
    conn, ender = s.accept()
    print ('Conectado em ', ender)

    data = conn.recv(1024)

    if data:
        message = data.decode()
        length_message = len(message)

        if length_message >= 10:
            conn.sendall(str.encode(random_string(length_message)))
        else:
            if int(message) % 2 == 0:
                conn.sendall(str.encode("PAR"))
            else:
                conn.sendall(str.encode("ÍMPAR"))
        print ('Fechando a conexão \n')
        conn.close()