#Q3. Even, Odd and Prime Checker
#Write a program using function to check whether 
#a number is even/odd and prime.

# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Main program
number = int(input("Enter a number: "))

# Check even/odd
even_odd = check_even_odd(number)

# Check prime
prime = is_prime(number)

# Display results
print("\n--- Number Analysis ---")
print(f"Number: {number}")
print(f"Status: {even_odd}")
if prime:
    print(f"Prime: Yes")
else:
    print(f"Prime: No")