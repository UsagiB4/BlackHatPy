import socket

# making of server

# AF_INET = ipv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 4434))
s.listen(5)

while True:
    clintsocket, address = s.accept()
    print(f"Address: {address}")
    clintsocket.send(bytes("welcome to the rice field", "utf-8"))
    clintsocket.close()