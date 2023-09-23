# Approach 1: Using a new string variable
def remove_char(string, n):
    if n >= len(string):
        return string
    new_string = ''
    for i in range(len(string)):
        if i != n:
            new_string += string[i]
    return new_string

# Approach 2: Using string slicing
def remove_char2(string, n):
    if n >= len(string):
        return string
    return string[:n] + string[n+1:]

# Approach 3: Using the replace method
def remove_char3(string, n):
    if n >= len(string):
        return string
    char_to_remove = string[n]
    return string.replace(char_to_remove, '', 1)

# Approach 4: Using a list and the del statement
def remove_char4(string, n):
    if n >= len(string):
        return string
    char_list = list(string)
    del char_list[n]
    return ''.join(char_list)

string = 'hello world'
n = 3

print(remove_char(string, n))   
print(remove_char2(string, n))  
print(remove_char3(string, n)) 
print(remove_char4(string, n))  