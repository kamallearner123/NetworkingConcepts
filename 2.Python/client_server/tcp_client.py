import os,sys,socket
from common import *

#1) Creating socket

s = socket.socket()

#2) Connect to server
s.connect((IPADDR, PORT))

s.send("hello".encode("ASCII"))

print(s.recv(1000))

s.close()
