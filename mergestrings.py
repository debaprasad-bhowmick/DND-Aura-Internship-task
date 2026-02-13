s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = ""
i = 0

while i < len(s1) and i < len(s2):
    result = result + s1[i] + s2[i]
    i = i + 1

# If strings are of unequal length
result = result + s1[i:] + s2[i:]

print("Merged string:", result)