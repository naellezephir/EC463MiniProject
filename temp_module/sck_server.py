import os
import socket
import sys
import json

HOST = '127.0.0.1'
PORT = 6543
serv_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(serv_address)
sock.listen()
conn, addr = sock.accept()
print('Connected with ', addr)

while True:
	data = conn.recv(1024)
	if not data:
		break;
	conn.sendall(b'Data Recieved')

sock.close()
print('Socket closed')