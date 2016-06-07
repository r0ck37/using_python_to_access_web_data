#!/usr/bin/python3

import socket

mysock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(str.encode('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')) #using str.encode to convert str to bytes

while True:
             data = mysock.recv(512)
             if ( len(data) < 1):
                 break
             print (data)
mysock.close()
             
