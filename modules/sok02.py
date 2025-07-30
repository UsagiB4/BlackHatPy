# ====== || Cleint || ======
import socket

HOST = "127.0.0.1"
PORT = 6673

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    sc.connect((HOST, PORT))
    sc.sendall(b"Hi from the client. \n\r python: is cool")
    data = sc.recv(1024)

print(f"Recieved data = {data!r}")