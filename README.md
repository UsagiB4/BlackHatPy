# What is this?
well, good question. Nothing special. Just me learning Python again but this time, for Hacking.

I'm Using the book called, **BlackHat Python 2nd Ed**.

I will keep notes while following the codes from the book and try to explain them.

>>> [Firstcode](code1.py)
### Key-Points:
- `AF_INET`: this tells the program that we are about to use ***IPv4***.
- `SOCK_STREAM`: this tells the code to act as a ***TCP Client***.
- `.connect()`: function to connect with the provided **IP** and the **PORT**
- `.send()`: function to send data as **RAW Binary** (as we used `(b"...")`).
- `.recv(4096)`: we receive the response from the server. the value `4096` indicates that we will receive **4096** bytes each time.
- `.decode()`: we have to use this function to decode the received data.
- `.close()`: closing the client.

---
---

>>> [Secondcode](code2.py)
### Key-Points: (UDP Client)
- `.SOCK_DGRAM`: socket type for **UDP**.
- `.sendto(b"message", (host, port))`: Since *UDP* is connection less protocol, we can send data without connecting using `.connect()`.
- `.recvfrom()`: is to receive data from *UDP*.

>>> [Thirdcode](code3.py)
### Key-Points: (TCP Server)
- `.bind((IP, PORT))`: Passing the IP and PORT we want the server to listen to.
- `.listen(5)`: starting the server. 5 refers to the number of backlog. *backlog* is simply how many pending connection we want to have.
- `.accept()`: receiving client's socket. Here we get 2 things, `client` that refers to client's socket type and `address` relative address for the client socket type. for IPv4, we get **IP** and **Port**.
- `threading` and `.Thread()`: As we are taking multiple connections, we need to switch to threading to handle each and every requests. here `.Thread(target=handle_client, args=(client,))` creates new execution path for a connection. Here `target=handle_client` is the function that the thread will run and `args=(client,)` is the argument that will be passed into that funciton.
  - > Noticed that comma after `client`? well, it's because argument should be a tuple. With that comma, it means, it's a single element tuple.