#!/usr/bin/python3
"""
PY6 Lab1 : Server Socket
"""

import socket
my_sock = socket.socket()  # Create the socket variable


my_sock.bind(("0.0.0.0", 4444))  # Bind the socket to accept connection from any IP on port 4444

my_sock.listen(1)  # Allow only one connection to the socket

connection, address = my_sock.accept()  # Allow a connection to the socket and save the connection object & address to variables


my_sock.close()  # Close the connection
