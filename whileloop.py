string = input("Enter a string: ")

rev = ""
i = len(string) - 1

while i >= 0:
    rev = rev + string[i]
    i = i - 1

print("Reversed string is:", rev)