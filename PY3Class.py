"""
Labs for Class 3
"""

############
# Lab 1
############

#upper_bound = int(input("Choose the range upper bound: ")) # Ask user for range upper limit

# iterate through the range specified
#for x in range(1, upper_bound):
#    print(f"The next number in the line is: {x}")



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