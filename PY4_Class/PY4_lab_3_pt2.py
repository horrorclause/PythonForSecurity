""""
Lab3 Pt.2: Handling Files

Part 2 of 2 files. This file opens the "test" file
"""

try:

    file = open("file.txt", "a")

    while True:
        message = input("Enter Text! ('Exit' to exit): ")
        if message.lower() == "exit":
            print("Exiting")
            break
        else:
            file.write(message + "\n")
    file.close()

except:
    print("An error occurred while trying to open the file.")

