import os,sys,socket

#1) Createing socket
s = socket.socket()

#2) bind to the ip and port
s.bind(("192.168.0.164", 6677))

#3) Listening
s.listen(10)

#4) Accept

while True:
    c,c_ip = s.accept()
    print("Client detaisl", c)
    print(dir(c))
    print(c.recv(1000))
    c.send("Hello")
    c.close()

