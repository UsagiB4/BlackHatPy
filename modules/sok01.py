import socket
# ====== || Server || ======
HOST = '127.0.0.1'
PORT = 6673

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    sc.bind((HOST, PORT))
    sc.listen()
    conn, addr = sc.accept()
    print(conn)
    with conn:
        print(f"connected to {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)