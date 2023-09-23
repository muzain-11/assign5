def add_ing_ly(string):
    if len(string) < 3:
        return string
    elif string.endswith('ing'):
        return string + 'ly'
    else:
        return string + 'ing'

print(add_ing_ly('abc'))     
print(add_ing_ly('string'))  