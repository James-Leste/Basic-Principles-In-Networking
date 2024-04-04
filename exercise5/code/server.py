import socket

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received from client: {message}")
        client_socket.send(f"Server Echo: {message}".encode('utf-8'))
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('35.204.255.227', 1234))
server_socket.listen()
print("Server is listening for connections...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")
    handle_client(client_socket)
