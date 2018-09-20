import os
import socket
import sys
import json
import mysql.connector
import time

# Socket details
HOST = '127.0.0.1'
PORT = 6543
serv_address = (HOST, PORT)

# Open connection to database
serv_database = mysql.connector.connect(
	host = os.environ['RDS_HOSTNAME'],
	user = os.environ['RDS_USERNAME'],
	password = os.environ['RDS_PASSWORD'],
	database = os.environ['RDS_DB_NAME'],
	port = os.environ['RDS_PORT'])

TABLE = 'room_data'

# Add cursor to edit database
serv_cursor = serv_database.cursor()

# Open and bind socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(serv_address)

while True:
	# Listen for access and record message
	sock.listen()
	conn, addr = sock.accept()
	print('Connected with ', addr)

	# Load in the message
	while True:
		raw_data = conn.recv(1024)
		if not raw_data:
			break; # When message ends, exit loop
		conn.sendall(b'Data Recieved\n') # Acknowledge data recieved to client

	# Unserialize json string
	clean_data = json.loads(raw_data)

	# Can now sort data to be inserted into table
	unit_id = clean_data(1)
	timestamp = clean_data(2)
	data_type = clean_data(3)
	owner = clean_data(4)
	value = clean_data(5)

	# Now to format into SQL language!
	sql = "INSERT INTO %s (owner, unit, times, type, value) VALUES (%s, %s, %s, %s, %s)"
	val = (TABLE, owner, unit_id, timestamp, data_type, value)

	# Time to append!!
	serv_cursor.execute(sql, val)
	serv_database.commit()
	conn.sendall(serv_cursor.rowcount, " Record inserted.\n")



sock.close()
print('Socket closed')