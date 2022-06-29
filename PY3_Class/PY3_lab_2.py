#!/usr/bin/python3

############
# Lab 2
############
# Create 1 list with 7 Classrooms with 10 students each ex. [[0,1,2,3,..], [0,1,2,3,...]]

classroom = []  # Empty list to store our 7 Classrooms

for i in range(7):  # Will create one classroom each iteration
    classroom.append([])  # Adds an empty list
    for students in range(1, 11):  # Adds 10 students to the classroom added during this iteration
        classroom[i].append(students)


# Using enumerate can help us count out the 7 classrooms. Using "start" lets us begin counting at 1 instead of 0
for iteration, c in enumerate(classroom, start=1):
    print(f"Class #{iteration} is {c}")