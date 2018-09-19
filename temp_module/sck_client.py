import os
import socket
import sys

# Update host and port w/ ACTUAL host/port values
HOST = 'localhost' #'http://miniproject-env.f9qrjzqsbn.us-east-1.elasticbeanstalk.com/'
PORT = 6543

# Create TCP/IP socket of type internet format stream
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect socket to server
server_address = (HOST, PORT)
print('HOST: {} PORT: {}'.format(*server_address))
sock.connect(server_address)

# Open json file and serialize
with open("temp_data.json") as read_file:
    data = read_file.read()
    try:
        #send data
        print('Message: {!r}'.format(data))
        sock.sendall(data.encode())

        #data acknowledgement
        ack = sock.recv(1024)
        print(ack)

    finally:
        print('close socket')
        sock.close()
