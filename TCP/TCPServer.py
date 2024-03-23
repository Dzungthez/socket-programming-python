import socket
import threading
import tkinter

HOST = '192.168.1.75'
PORT = 8000  # optional
SERVER_LIMIT = 5
active_clients = []


def listen_for_messages(client, username):
    while 1:
        response = client.recv(2048).decode('utf-8')
        if response != '':
            final_msg = f'{username}~{response.upper()}'
            send_messages_to_all(final_msg)
        else:
            print(f'Client {username} message is empty')


# send msg to a single client
def send_message_to_client(client, message):
    client.sendall(message.encode('utf-8'))


# send new msg to all the clients that are currently connected
def send_messages_to_all(message, type='server'):
    for user in active_clients:
        send_message_to_client(user[1], message)


def client_handler(client):
    # server will listen for client's message that contains the username
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            print(f"Client {username} has connected")

            # send a welcome message to the client
            welcome_msg = f" \n [SERVER]~Welcome to the chat room, {username}! \n"
            send_messages_to_all(welcome_msg)
            break
        else:
            print('Client username is empty')
    threading.Thread(target=listen_for_messages, args=(client, username,)).start()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        print(f"Server bound to host {HOST} and port {PORT}")

    except:
        print(f"Server failed to bind to host {HOST} and port {PORT}")
        return
    # set server limit
    server.listen(SERVER_LIMIT)
    while 1:
        client, address = server.accept()
        # address[0] is the IP address, address[1] is the port
        print(f"Connected to {address[0]}, {address[1]}")
        # this thread keeps running until the client disconnects
        threading.Thread(target=client_handler, args=(client,)).start()


if __name__ == "__main__":
    main()
