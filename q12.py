#Q12. Sum of Digits
#Find the sum of digits of a number using while loop.

# Input a number
num = int(input("Enter a number: "))

# Convert to positive if negative
num = abs(num)

# Calculate sum of digits
digit_sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp = temp // 10

# Display results
print("\n--- Sum of Digits ---")
print(f"Number: {num}")
print(f"Sum of digits: {digit_sum}")