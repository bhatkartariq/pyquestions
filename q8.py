#Q8. List Operations
#Create a list of numbers and 
#perform append, remove and sort operations.

# Create a list of numbers
numbers = [5, 2, 8, 1, 9, 3]
print("Original list:", numbers)

# Append operation
numbers.append(7)
print("After append(7):", numbers)

# Remove operation
numbers.remove(2)
print("After remove(2):", numbers)

# Sort operation
numbers.sort()
print("After sort():", numbers)

# Reverse sort
numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)