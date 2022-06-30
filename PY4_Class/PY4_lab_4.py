""""
Lab4: Extracting Lines

"""

path = input("Enter a directory path for the text file: ")
filename = input("Enter full filename: ")

file = open(path+'\\'+filename, 'r')

for line in file:
    print(line)

file.close()

input("\n Press 'Enter' to exit.")