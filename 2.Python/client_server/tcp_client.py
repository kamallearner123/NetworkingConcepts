import os,sys,socket

#1) Creating socket

s = socket.socket()

#2) Connect to server
s.connect(("192.168.0.164", 6677))

s.send("hello".encode("ASCII"))

print(s.recv(1000))

s.close()
