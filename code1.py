import socket

target_host = "127.0.0.1"
target_port = 6673

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

resp = client.recv(1024)
print(resp.decode())
client.close()