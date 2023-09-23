def count_repeated_characters(string):
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char, frequency in count.items():
        if frequency > 1:
            print(char, frequency)

count_repeated_characters('thequickbrownfoxjumpsoverthelazydog')
