import socket
import threading

# Client configuration
HOST = '127.0.0.1'
PORT = 5555

nickname = input("Choose a nickname: ")

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        msg = f"{nickname}: {input('')}"
        client.send(msg.encode('utf-8'))

# Threads for sending & receiving
thread1 = threading.Thread(target=receive)
thread1.start()

thread2 = threading.Thread(target=write)
thread2.start()
