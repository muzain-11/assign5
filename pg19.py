def find_smallest_and_largest_word(string):
    words = string.split()
    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)
    return smallest_word, largest_word

sample_string = 'thequickbrownfoxjumpsoverthelazydog'
smallest_word, largest_word = find_smallest_and_largest_word(sample_string)
print(f'Smallest word: {smallest_word}')
print(f'Largest word: {largest_word}')
