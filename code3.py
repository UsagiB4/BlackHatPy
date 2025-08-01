import socket
import threading

IP = "127.0.0.1"
port = 6673

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, port))
    server.listen(5)
    print(f'[*] Listening on {IP}:{port}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recieved: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()