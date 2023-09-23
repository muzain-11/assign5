def swap_comma_and_dot(string):
    return string.translate(string.maketrans(',.', '.,'))

sample_string = "32.054,23"
output_string = swap_comma_and_dot(sample_string)
print(output_string)
