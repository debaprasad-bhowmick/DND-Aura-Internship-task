s = input("Enter a string: ")
s = s.lower()

vowels = "aeiou"

for v in vowels:
    count = s.count(v)
    print(f"{v} : {count}")
