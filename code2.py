import socket

target_host = "127.0.0.1"
target_port = 6673

client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"hello from client UDP", (target_host, target_port))

data, addr = client.recvfrom(2024)

print(data.decode())
print(addr)
client.close()