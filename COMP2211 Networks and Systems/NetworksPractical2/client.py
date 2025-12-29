import socket

clientID = "client-1"

def start_client(address):
    while True:
        message = input(">> ")  
        with socket.socket() as s:
            s.connect(address)    # The method enables the sender's socket to connect to the destination socket; address is a Tuple which includes both IP address and port number of the destination
            fullMessage = clientID + "|||" + message
            s.sendall(fullMessage.encode())  # sendall: send the entire buffer you have or throw an exception. message.encod: covert the message to binary streams.

def start():
    start_client(("127.0.0.1",8080))

if __name__ == "__main__":
    start()