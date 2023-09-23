string = input("Enter a string: ")
freq = {}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("The character frequency of the string is", freq)
