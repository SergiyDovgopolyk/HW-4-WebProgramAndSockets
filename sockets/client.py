import socket

def client():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input('--> ')
        client_socket.sendto(message.encode(), (host, port))

        if message.lower().strip() == 'end':
            break

    client_socket.close()

if __name__ == '__main__':
    client()

