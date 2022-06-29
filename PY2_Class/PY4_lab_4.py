#!/usr/bin/python3

"""
Lab 4 Exercise
"""

# Construct an interactive script that returns which service is associated with which port number.

protocolsDict = {
    'FTP': '20, 21',
    'SSH': '22',
    'Telnet': '23',
    'SMTP': '25',
    'DNS': '53',
    'DHCP': '67, 68',
    'POP3': '110',
    'IMAP4': '143',
    'NetBIOS': '137, 138, 139',
    'LDAP': '389',
    'SMB': '445',
    'HTTP': '80',
    'HTTPS': '443',
    'MySQL': '3306'
}
# Added .upper() so it changes input to uppercase to be read in the dictionary
question = input("Which protocol do you want to know the port number for? : ").upper()

if question in protocolsDict.keys():
    answer = protocolsDict[question]
    print(f"The port number for {question} is {answer}.")
else:
    print(f"The port number for {question} cannot be found.")