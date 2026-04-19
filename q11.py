#Q11. Word and Line Counter
#Read a text file and count number of words and lines.

# Input filename
filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        word_count = 0
        line_count = len(lines)
        
        for line in lines:
            words = line.split()
            word_count += len(words)
        
        # Display results
        print("\n--- File Statistics ---")
        print(f"Filename: {filename}")
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")