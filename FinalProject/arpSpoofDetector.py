#!/usr/bin/python3

"""ARP Spoof Detector - will find IP addresses with duplicate MACs"""

import os

# This function pulls the ARP table


def arpTableExtraction():
    arp_table = os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()
    #print(arp_table_lines)
    addresses = {}

    # If broadcast is found, break the function, we have reached the end of the entries
    for line in arp_table_lines:
        if "ff-ff-ff-ff-ff-ff" in line or "ff:ff:ff:ff:ff:ff" in line:
            break

        # Begins at index 2 where the IP, MAC, and TYPE entries are recorded
        if arp_table_lines.index(line) > 2:
            ip, mac, _type = line.split()
            addresses[ip] = mac

    return addresses


#print(arpTableExtraction())

def identify_duplication(addresses):
    pass