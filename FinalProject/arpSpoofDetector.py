#!/usr/bin/python3

"""ARP Spoof Detector - will find IP addresses with duplicate MACs"""

import os
import time
from datetime import datetime

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

    identify_duplication(addresses)


#print(arpTableExtraction())

# This will identify duplicate MACs in the extracted addresses
def identify_duplication(addresses):
    tmp_mac_lst = []
    print("Scanning....")
    time.sleep(2)

    for mac in addresses.values():
        if mac in tmp_mac_lst:
            print("Finished scanning!")
            create_log(f"Arp spoofed!\nThe address is: {mac}")
            break
        tmp_mac_lst.append(mac)
    #print("Nothing found")


# This will create the log file to record the MAC spoof.
def create_log(message):
    print("Generating logs...")
    time.sleep(2)
    date = datetime.now()

    with open("log.txt", "a") as log:
        log.write(f"{message}\nDate: {date}\n\n")

    print("The event is logged in log.txt")


if __name__ == "__main__":
    arpTableExtraction()
