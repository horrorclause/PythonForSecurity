#!/usr/bin/env python3
"""
PY6 Lab4: Implement authentication and verify incoming connections.

Server-side
"""
import socket

s = socket.socket()
s.bind(("0.0.0.0", 4321))
s.listen(1)
conn, addr = s.accept()

conn.send("Welcome to the server!\nPlease insert your Username:".encode())

username = conn.recv(2048).decode()

conn.send("Please enter your password: ".encode())

passwd = conn.recv(2048).decode()

if username == "John" and passwd == "12345":
    conn.send(f"Welcome {username}!".encode())
else:
    conn.send("You have entered the wrong credentials.".encode())

s.close()

