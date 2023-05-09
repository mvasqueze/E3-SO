import socket
import threading

# define host and port
HOST = 'localhost'
PORT = 5555

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set socket option to reuse address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind socket to a specific address and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()

# list to keep track of connected clients
clients = []

def broadcast(message):
    # send a message to all connected clients
    for client in clients:
        client.send(message)

def handle_client(client_socket, address):
    # get client's name
    name = client_socket.recv(1024).decode('utf-8')
    # add client to list of connected clients
    clients.append(client_socket)
    # send a welcome message to the client
    welcome_message = f"-------------Welcome {name}!-------------"
    broadcast(welcome_message.encode('utf-8'))

    while True:
        try:
            # receive message from client
            message = client_socket.recv(1024)
            # broadcast message to all other clients
            broadcast(message)
        except:
            # remove client from list of connected clients
            clients.remove(client_socket)
            # send a leave message to other clients
            leave_message = f"-------------{name} has left the chat.-------------\n"
            broadcast(leave_message.encode('utf-8'))
            # close connection
            client_socket.close()
            break

print(f"Server is listening on {HOST}:{PORT}...")

while True:
    # accept incoming connection
    client_socket, address = server_socket.accept()
    # create a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
