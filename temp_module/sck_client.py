import os
import socket
import sys
import json

# Open json file and serialize
open("temp_data.json") as read_file

# Update host and port w/ ACTUAL host/port values
HOST = 'localhost'
PORT = 1000

# Create TCP/IP socket of type internet format stream
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect socket to server
server_address = (HOST, PORT)
print('HOST: {} PORT: {}'.format(*server_address))
sock.connect(server_address)

try:
    #send data
    print('Message: {!r}'.format(data))
    sock.sendall(data)

    #response detection
    amount_recieved = 0
    amount_expected = len(data)

    while(amount_recieved < amount_expected):
        rcv_data = sock.recv(16)
        amount_recieved += len(rcv_data)
        print('Recieved {!r}'.format(rcv_data))

finally:
    print('close socket')
    sock.close()
