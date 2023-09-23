def remove_consecutive_duplicates(string):
    return ''.join(i for i, _ in itertools.groupby(string))

sample_string = 'thequickbrownfoxjumpsoverthelazydog'
output_string = remove_consecutive_duplicates(sample_string)
print(output_string)
