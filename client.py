import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))

print(s.recv(2048).decode("utf-8"))
msg = "Hosbulduk efenim..."
s.send(msg.encode("utf-8"))
while True:
    print("Ben: ")
    print(s.send(input().encode("utf-8")))
    print("O: ")
    print(s.recv(2048).decode("utf-8"))
s.close()
