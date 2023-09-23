def longest_length(words):
    longest_word = max(words, key=len)
    return len(longest_word)

word_list = ['one', 'two', 'three', 'four']
print(longest_length(word_list))  
