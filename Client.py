import socket
import threading

HOST = '127.0.0.1'
PORT = 65432     

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Ошибка при получении сообщения. Соединение закрыто.")
            client_socket.close()
            break

def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages)
    send_thread.start()