import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.bind(("10:63:c8:39:27:3c", 4)) # Cambiar por la dirección MAC Bluetooth correcta y disponible en el equipo local

try:
    client.connect(("f0:9e:4a:ae:a3:9d", 4)) # Cambiar por la dirección MAC Bluetooth correcta y disponible en el equipo remoto
    print("Conexión establecida.")
    while True:
        message = input("Ingrese un mensaje: ")
        client.send(message.encode('utf-8'))
        data = client.recv(1024)
        if not data:
            break
        print(f"Mensaje recibido: {data.decode('utf-8')}")
except OSError as e:
    print(f'Error: {e}')
    pass

client.close()
