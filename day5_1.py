#Calculating average height with for loop

#Initialization
student_heights = input("Input a list of students height \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

#The sum loop
total_height = 0  #Declare an outside variable to add the elements of student_heights to
for height in student_heights:
    total_height += height
# print(total_height)


#The length loop
student_number = 0
for student in student_heights:
    student_number += 1
# print(student_number)

average = round(total_height / student_number)
print(average)