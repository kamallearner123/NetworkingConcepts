import os,sys,socket
from common import *
#1) Createing socket
s = socket.socket()

#2) bind to the ip and port
s.bind((IPADDR, PORT))

#3) Listening
s.listen(10)

#4) Accept

while True:
    c,c_ip = s.accept()
    print("Client detaisl", c, c_ip)
    print(c.recv(1000))
    c.send("Hello")
    c.close()

