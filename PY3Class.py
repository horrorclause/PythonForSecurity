"""
Labs for Class 3
"""

############
# Lab 1
############

upper_bound = int(input("Choose the range upper bound: ")) # Ask user for range upper limit

# iterate through the range specified
for x in range(1, upper_bound):
    print(f"The next number in the line is: {x}")



############
# Lab 2
############

classroom = [] # Empty list to store our 7 Classrooms

for i in range(7):  # Will create one classroom each iteration
    classroom.append([])  # Adds an empty list
    for students in range(1, 11):  # Adds 10 students to the classroom added during this iteration
        classroom[i].append(students)


# Using enumerate can help us count out the 7 classrooms. Using "start" lets us begin counting at 1 instead of 0
for iteration, c in enumerate(classroom, start=1):
    print(f"Class #{iteration} is {c}")



############
# Lab 3
############

counter = 0

while counter < 10:
    counter += 1
    if counter == 6:
        print("Found")
        break

    else:
        print(f"Check {counter}")


############
# Lab 4
############

servicePorts = {}

while True:
    service = input("Please enter a service's name or type '0' to stop: ")
    if service == "0":
        print("Stopping...")
        break

    port = input("Please enter a port number or type '0' to stop: ")
    if port == "0":
        break

    servicePorts[service] = port

print(servicePorts)


############
# Lab 5
############