# Write a Python function print_student_averages(grades) that takes a 2D list where each inner list represents a student's grades in different subjects. The function should print each student's grades and their average grade. 



def print_student_averages(grades):
    
    grades = []
    row = int(input("Enter the number of students: "))
    column = int(input("Enter the number of subjects: "))
    
    for i in range(row):
        scores = []
        print(f"Enter grades for student {i + 1}:")
        for j in range(column):
            scores.append(int(input(f"Grade for subject {j + 1}: ")))
        grades.append(scores)
    
    for i in range(row):
        print(f"\nStudent {i + 1} grades: {grades[i]}")
        average = sum(grades[i]) / column
        print(f"Average grade for student {i + 1}: {average:}")

print_student_averages([])













# def print_student_averages(grades):
    
#     grades = []
#     row = int(input("Enter the number of students: "))
#     column = int(input("Enter the number of Subjects: "))
    
#     for i in range(row):
#         scores = []
#         for j in range(column):
#             scores.append(int(input()))
#         grades.append(scores)
#     # return grades

#     for i in range(row):
#         for j in range(column):
#             print(grades[i][j], end=" ")
#         print()
#     return grades

# print_student_averages([])