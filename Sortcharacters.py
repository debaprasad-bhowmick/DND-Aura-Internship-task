s = input("Enter a string: ")

alphabets = []
digits = []

for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    elif ch.isdigit():
        digits.append(ch)

alphabets.sort()
digits.sort()

result = "".join(alphabets + digits)
print("Sorted string:", result)