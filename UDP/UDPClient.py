import socket
import threading

HOST = '127.0.0.1'
PORT = 12000


def listen_for_messages_from_server(client):
    try:
        # Receive message from the server
        message, _ = client.recvfrom(2048)
        print(f"[SERVER]: {message.decode('utf-8')}")
    except OSError as e:
        print(f"OS error: {e}")


def send_message_to_server(client):
    message = input()
    if message != '':
        try:
            client.sendto(message.encode('utf-8'), (HOST, PORT))
        except OSError as e:
            print(f"OS error: {e}")
    else:
        print('Message is empty')


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        send_message_to_server(client)
        listen_for_messages_from_server(client)


if __name__ == '__main__':
    main()
