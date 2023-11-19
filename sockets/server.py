import socket
import json
from datetime import datetime

def main():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    while True:
        data, addr = server_socket.recvfrom(1024)
        received_data = data.decode()
        print(f"Received message: {received_data} from {addr}")

        if received_data.lower().strip() == 'end':
            break

        parsed_data = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "message": received_data
        }

        with open('storage/data.json', 'a+') as file:
            json.dump(parsed_data, file)
            file.write('\n')

    server_socket.close()

if __name__ == '__main__':
    main()