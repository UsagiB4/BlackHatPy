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
### Key-Points:
- 