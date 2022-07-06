#!/usr/bin/env python3
"""
PY6 Lab3 pt.1: Test Communication

Server script
"""

import socket

sock = socket.socket()

sock.bind(("0.0.0.0", 45000))   # Bind the socket to accept connections from all IPs on 45000

sock.listen(1)   # Accept only one connection to the socket

conn, addr = sock.accept()  # Allow the server to accept connection, and save the connection objects to variables

conn.send("Welcome to the server!".encode())    # Encode the message sent to the client

print(conn.recv(2048).decode())  # Accept a message from the client and print it

sock.close()    # Close the connection

