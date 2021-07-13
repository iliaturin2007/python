#!/bin/python3

import socket, random

ip = '127.0.0.1'

port = 10000

sock = socket.socket()

sock.bind((ip, port))

sock.listen()

print("Server is started")
print("Addres is", str(port)+':'+ip)
print("\n")

clientSock, clientAddr = sock.accept()



for i in range(10):
	clientSock.send("Hallo, i'm server\n".encode())
