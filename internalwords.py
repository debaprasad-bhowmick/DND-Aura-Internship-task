string = input("Enter a string: ")

words = string.split()
rev_words = []

for word in words:
    rev_words.append(word[::-1])

result = " ".join(rev_words)

print("Output:", result)