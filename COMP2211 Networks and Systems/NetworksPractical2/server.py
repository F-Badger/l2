import socket

clientTable = []
maxMessages = 3

def start_server(address):
    with socket.socket() as s:

        # assigns the IP address and the port number to this socket instance
        s.bind(address) 

        # 1 specifies the number of unaccepted connections that the system will allow before refusing new connections
        s.listen(1)  
        
        while True:
            connection, (peer_ip, _) = s.accept()  # Wait for a new connection to come in and Establish a socket for communications if so. accept() returns a socket of the other side on this connection. 
            with connection:
                fullMessage = connection.recv(1024).decode()
                messageParts = fullMessage.split("|||")
                clientID = messageParts[0]
                knownClient = False
                reachedMessageLimit = False
                for client in clientTable:
                    if client[0] == clientID:
                        knownClient = True
                        print (client)
                        if client[1] == 0:
                            print("Client {} - do not send any more messages".format(peer_ip))
                            reachedMessageLimit = True
                            continue
                print (f"known: {knownClient}")
                if not knownClient:
                    clientTable.append([clientID, maxMessages])
                if not reachedMessageLimit:
                    message = messageParts[1]
                    print("{}: {}".format(peer_ip, message))
                    for client in clientTable:
                        if client[0] == clientID:
                            client[1] -= 1
                            continue

def start():
    start_server(("",8080))

if __name__ == "__main__":
    start()