# Input two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# Check anagram
if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
