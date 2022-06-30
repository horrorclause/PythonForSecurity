import os
""""
Lab5: File System & Error Handling
"""

file_name = input("Choose a filename: ")
# For mac and linux systems add -c 4 flag
os.system(r"ping 8.8.8.8 >> "+file_name+'.txt')

with open(file_name + '.txt', 'r') as file:
    if "ms" in file.read():
        print("You have an internet connection")
    else:
        print("You don't have an internet connection")
