import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 4434))

while True:
    mesg = s.recv(32)
    if len(mesg) <= 0:
        break
    else:
        print(mesg.decode('utf-8'))