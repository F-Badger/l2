import socket

HOST = "127.0.0.1"
PORT = 8000
CLIENTID = "client-1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        message = input(">> ")
        fullMessage = CLIENTID + "|||" + message
        s.sendall(fullMessage.encode())