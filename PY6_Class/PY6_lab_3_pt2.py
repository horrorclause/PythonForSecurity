#!/usr/bin/env python3
"""
PY6 Lab3 pt.2: Test Communication

Client script
"""

import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 45000))  # Connect the socket to the listened in the server
print(sock.recv(2048).decode())  # Receive the server message, decode it, and print it
sock.send("Thanks!".encode())   # Return message, notifying client received server message
sock.close()    # Closing the connection
