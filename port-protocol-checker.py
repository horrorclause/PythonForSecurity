"""
Give it a port number and it will return a protocol;
Give it a protocol and it will return a port number.
"""

import socket

#takes input from user, either port number or protocol name
question = input("Which protocol do you want to know the port number for? : ").lower()


def portChecker(name):

    if name.isdigit():  # checks to see if input is a digit
        try:
            portNum = socket.getservbyport(int(name))  # returns protocol name
            return portNum

        except OSError:
            return "cant find protocol"

    elif name.isalpha():  # checks to see if input is a digit
        try:
            protocolName = socket.getservbyname(name)  # returns port number
            return protocolName

        except OSError:
            return "cant find port number"

    else:
        return "Please enter either a protocol or port number"


print(portChecker(question))

