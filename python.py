# Student Marks Management System

print("===== STUDENT MARKS MANAGEMENT SYSTEM =====")

name = input("Enter Student Name: ")

python = float(input("Enter Python Marks: "))
maths = float(input("Enter Maths Marks: "))
ai = float(input("Enter AI Marks: "))

total = python + maths + ai

percentage = total / 3

if python < 35 or maths < 35 or ai < 35:
    grade = "Fail"
elif percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "D"

print("\n===== STUDENT RESULT =====")

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

if grade == "Fail":
    print("Result: FAIL")
else:
    print("Result: PASS")
