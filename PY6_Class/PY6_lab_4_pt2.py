"""
PY6 Lab4: Implement authentication and verify incoming connections.

Client-side
"""
import socket

s = socket.socket()
s.connect(("127.0.0.1", 4321))
print(s.recv(2048).decode())

s.send(input("").encode())  # Send username

print(s.recv(2048).decode())

s.send(input("").encode())  # Send password

print(s.recv(2048).decode())

s.close()
