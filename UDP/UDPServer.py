import socket
import threading

HOST = '127.0.0.1'
PORT = 12000


def listen_for_messages(server):
    while True:
        # Receive message and client's address
        message, clientAddress = server.recvfrom(2048)
        final_msg = message.decode('utf-8')
        if final_msg:
            print(f"Received message from {clientAddress}: {final_msg}")
            final_msg = final_msg.upper()
            # send back
            server.sendto(final_msg.encode('utf-8'), clientAddress)
            print('Sent message back to client')
        else:
            print(f"Received empty message from {clientAddress}")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        server.bind((HOST, PORT))
        print(f"UDP server up and listening at {HOST}:{PORT}")
    except:
        print(f"Failed to bind to {HOST}:{PORT}")
        return

    threading.Thread(target=listen_for_messages, args=(server,)).start()


if __name__ == "__main__":
    main()
