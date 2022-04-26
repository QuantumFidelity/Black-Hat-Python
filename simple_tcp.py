# This is a simple TCP client written in Python. 

import socket

target_host = "0.0.0.0"
target_port = 9999

str = "Passing this as byte code"
arr = bytes(str, 'utf-8')

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(arr)

#receive some data
response = client.recv(4096)

print(response)
