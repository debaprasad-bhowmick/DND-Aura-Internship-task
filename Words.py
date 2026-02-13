string = input("Enter a string: ")

words = string.split() 
rev = " ".join(words[::-1])

print("Reversed order of words:", rev)