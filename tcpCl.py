#!/usr/bin/python3

#this script assumes that port 80 on the host is always listening and is just for practice' sake

import socket

targHost = "www.google.com"
targPort = 80

#socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect
client.connect((targHost,targPort))

#send data to the host you want, I used google.com
client.send(b"GET /http://google.com\r\nHTTP/1.1")

#recv data
response = client.recv(8000)

print(response) 
