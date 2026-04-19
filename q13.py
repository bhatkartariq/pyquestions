#13. Number Pattern
#Print the pattern for n lines:
#1
#12
#123
#1234
#12345

# Input number of lines
n = int(input("Enter the number of lines: "))

print("\n--- Number Pattern ---")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()