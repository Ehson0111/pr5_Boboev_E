import socket
import threading

HOST = '127.0.0.1'  
PORT = 65432        

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Удаление отключившихся клиентов
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, client_socket)
        except:
            # Удаление отключившихся клиентов
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    print(f"Сервер запущен на {HOST}:{PORT}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

start_server()