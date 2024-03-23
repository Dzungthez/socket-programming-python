import socket
import threading
import tkinter as tk

TITLE = 'Chat Room v1.0'

HOST = '192.168.1.75'
PORT = 8000  # optional


def scene_setting():
    app = tk.Tk()
    app.title(TITLE)
    app.geometry('600x600')
    app.resizable(False, False)
    return app


def listen_for_messages_from_server(client, username):
    while 1:
        message = client.recv(2048).decode('utf-8')

        if message != '':
            username = message.split('~')[0]
            content = message.split('~')[1]

            print(f'[{username}]: {content}')
        else:
            print(f'Client {username} message is empty')


def send_message_to_server(client):
    while 1:
        message = input()
        if message != '':
            client.sendall(message.encode('utf-8'))
        else:
            print('sending message is empty')


def communicate_with_server(client):
    username = input("Enter your username: ")
    if username != '':
        client.sendall(username.encode('utf-8'))
    else:
        print('Username is empty')
        exit(0)

    threading.Thread(target=listen_for_messages_from_server, args=(client, username,)).start()
    send_message_to_server(client)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # must match server

    try:
        client.connect((HOST, PORT))
    except:
        print(f"Failed to connect to server at {HOST} and port {PORT}")
        return

    communicate_with_server(client)


if __name__ == '__main__':
    main()
