#Q9. Dictionary Student Record
#Store student names and marks in dictionary and
#display the student who scored highest marks.

# Create a dictionary of student records
students = {}

# Input number of students
n = int(input("Enter the number of students: "))

# Input student names and marks
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

# Find the student with highest marks
topper = max(students, key=students.get)
max_marks = students[topper]

# Display results
print("\n--- Student Records ---")
for name, marks in students.items():
    print(f"{name}: {marks}")

print(f"\nTopper: {topper} with {max_marks} marks")