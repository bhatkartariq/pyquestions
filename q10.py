#Q10. Multiplication Table
#Print multiplication table of a given number using loop.

# Input a number
num = int(input("Enter a number: "))

print(f"\n--- Multiplication Table of {num} ---")
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")