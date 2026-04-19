#Q5. Star Pattern Printing
#Print the following pattern for n lines:
#*
#**
#***
#****

# Input number of lines
n = int(input("Enter the number of lines: "))

print("\n--- Star Pattern ---")
for i in range(1, n + 1):
    print("*" * i)