#Q14. Count Vowels and Consonants
#Count number of vowels and consonants in a given string.

# Input a string
string = input("Enter a string: ").lower()

# Count vowels and consonants
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Display results
print("\n--- Vowel and Consonant Count ---")
print(f"String: {string}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")