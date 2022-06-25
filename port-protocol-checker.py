import socket

question = input("Which protocol do you want to know the port number for? : ").lower()


def portChecker(name):

    if name.isdigit():
        try:
            portNum = socket.getservbyport(int(name))
            return portNum

        except OSError:
            return "cant find protocol"

    elif name.isalpha():
        try:
            protocolName = socket.getservbyname(name)
            return protocolName

        except OSError:
            return "cant find port number"

    else:
        return "Please enter either a protocol or port number"


print(portChecker(question))