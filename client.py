import socket
import threading
import random

# define host and port
HOST = 'localhost'
PORT = 5555

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client_socket.connect((HOST, PORT))

# prompt user for their name
name = input("Enter your name: ")

# assign a random color to the client's name
name_color = f"\033[{random.randint(31, 37)}m{name}\033[0m"

# send name to server
client_socket.send(f"{name_color}".encode('utf-8'))

def receive():
    while True:
        try:
            # receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            # check if message is sent by this client
            if not message.startswith(f"{name_color}:"):
                # display message
                print(message)
        except:
            # close connection if error occurs
            client_socket.close()
            break

# create a lock object
lock = threading.Lock()

def send():
    while True:
        message = input()
        # acquire the lock before sending the message
        with lock:
            # check if the socket is still open
            if client_socket.fileno() == -1:
                break
            # send message to server in the format "name: message"
            client_socket.send(f"{name_color}: {message}".encode('utf-8'))

# start separate threads to receive and send messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
