import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("00:1a:7d:da:71:13", 4))
#server.bind(("80:30:49:34:5c:fe", 4))
#80:30:49:34:5c:fe
#00:1a:7d:da:71:13
server.listen(1)

client, addr = server.accept()

print(f"Server is listening...")
try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
except OSError as e:
    print(f'Error: {e}')
    pass

client.close()
server.close()
