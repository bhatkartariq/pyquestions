#Q4. Factorial Using Recursion
#Find factorial of a number using recursion.

# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main program
number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"\n--- Factorial Result ---")
    print(f"Number: {number}")
    print(f"Factorial: {result}")