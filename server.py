import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
print("Server kuruldu: " + host + ":" + str(port))
s.bind((host,port))

s.listen(10)
while True:
    c,addr = s.accept()
    print(str(addr[0]) + " bağlandı")
    msg = "Hoşgeldiniz " + str(addr[0])
    c.send(msg.encode("utf-8"))
    dummy = c.recv(2048).decode("utf-8")
    print(dummy)
    
    while True:
        print("O: " )
        print(c.recv(2048).decode("utf-8"))
        print("Ben: ")
        print(c.send(input().encode("utf-8")))

c.close