#Q1. Student Result Calculator
#Write a Python program to accept marks of 3 subjects, calculate total and
#percentage, and assign grade using if-else.

# Input marks for 3 subjects
subject1 = float(input("Enter marks for Subject 1 (out of 100): "))
subject2 = float(input("Enter marks for Subject 2 (out of 100): "))
subject3 = float(input("Enter marks for Subject 3 (out of 100): "))

# Calculate total and percentage
total = subject1 + subject2 + subject3
percentage = (total / 300) * 100

# Assign grade based on percentage
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 50:
    grade = 'E'
else:
    grade = 'F'

# Display results
print("\n--- Student Result ---")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")