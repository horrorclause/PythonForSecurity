#!/usr/bin/env python3
"""
PY6 Lab2 : Client Socket
"""

import socket, time

my_sock = socket.socket()   # Creating the socket variable

my_sock.connect(("192.168.240.128", 4444))  # Connecting the socket to the listener

time.sleep(5)   # Pausing for 5 seconds

my_sock.close()  # Closing connection
