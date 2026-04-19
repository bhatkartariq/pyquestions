#Q6. Reverse Number Using While Loop
#Reverse a number and check whether it is palindrome.

# Input a number
number = int(input("Enter a number: "))

# Store original number
original = number

# Reverse the number using while loop
reversed_num = 0
while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10

# Check if palindrome
if original == reversed_num:
    is_palindrome = "Yes"
else:
    is_palindrome = "No"

# Display results
print("\n--- Number Reversal & Palindrome Check ---")
print(f"Original Number: {original}")
print(f"Reversed Number: {reversed_num}")
print(f"Is Palindrome: {is_palindrome}")