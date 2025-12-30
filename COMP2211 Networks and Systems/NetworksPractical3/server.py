import socket
import threading
import re

messageLimit = {
    "client-1": 5,
}
messagesSent = {
    "client-1": 0
}

def handle_client(connection, addr):
    print(f"[NEW CONNECTION] {addr}")
    with connection:
        while True:
            try:
                data = connection.recv(1024)
                if not data:
                    break  # client disconnected
            except:
                break
            
            fullMessage = data.decode()
            messageParts = fullMessage.split("|||")
            clientID = messageParts[0]
            message = messageParts[1]

            printMessage = True

            match = re.match(pattern=r'^\\setmessagelimit (\d+)$', string=message)

            if (match):
                newLimit = int(match.group(1))
                messageLimit[clientID] = newLimit
                printMessage = False
                print(f"Message limit for {clientID} updated to {newLimit}")

            if clientID not in messageLimit:
                messageLimit[clientID] = 5
                messagesSent[clientID] = 0
            else:
                if messageLimit[clientID] == messagesSent[clientID]:
                    print(f"No messages remaining for {addr}")
                    printMessage = False

            if printMessage:
                messagesSent[clientID] += 1
                messagesRemaining = messageLimit[clientID] - messagesSent[clientID]
                print(f"{clientID}: {message} ({messagesRemaining} messages remaining)")

    print(f"[DISCONNECTED] {addr}")

def start_server(address):
    with socket.socket() as s:
        s.bind(address) 
        s.listen()
        print(f"Listening at {address[0]}:{address[1]}")  
        
        while True:
            connection, (peer_ip, _) = s.accept()
            thread = threading.Thread(
                target=handle_client,
                args=(connection, peer_ip),
                daemon=True
            )
            thread.start()

def start():
    IP = "127.0.0.1"
    PORT = 8000
    start_server((IP,PORT))

if __name__ == "__main__":
    start()