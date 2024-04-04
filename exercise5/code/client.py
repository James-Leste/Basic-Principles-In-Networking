import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind(('localhost', 1233))
client_socket.connect(('35.204.255.227', 1234))
print('listening on port:', client_socket.getsockname()[1])

try:
    while True:
        message = input("Type your message (type 'quit' to exit): ")
        if message.lower() == 'quit':
            break
        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
finally:
    client_socket.close()
