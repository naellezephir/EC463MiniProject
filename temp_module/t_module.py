import os
import time
import socket
import sys

import json_export

# Timer Def
def sim_timer(time):
	while time:
		time.sleep(1)
		t -= 1
 
def generate(unit_id, owner):
	# Format: Unit ID, Date/time, type, owner, value
	timestamp = time.localtime()
	data = {
		"unit_id": unit_id,
		"date_time": [timestamp[0], timestamp[1], timestamp[2], timestamp[3], timestamp[4]],
		"type": "temperature",
		"owner": owner,
		"value": 50 # Replace w/ random value
	}
	return data

# Update host and port w/ ACTUAL host/port values
HOST = 'localhost'
PORT = 10000

# Create TCP/IP socket of type internet format stream
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect socket to server
server_address = (HOST, PORT)
print('HOST: {} PORT: {}'.format(*server_address))
sock.connect(server_address)

try:
	while True:
		#send data
		data = generate(650, "Kuro")
		print('Message: {!r}'.format(data))
		sock.sendall(data)

		#response detection
		amount_recieved = 0
		amount_expected = len(data)

		while(amount_recieved < amount_expected):
			rcv_data = sock.recv(16)
			amount_recieved += len(rcv_data)
			print('Recieved {!r}'.format(rcv_data))

		#add 20 sec timer
		sim_timer(20)

finally:
	print('close socket')
	sock.close()