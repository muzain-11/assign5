def string_both_ends(string):
    if len(string) < 2:
        return ''
    return string[0:2] + string[-2:]

print(string_both_ends('thisisniceone')) 
print(string_both_ends('ab'))            
print(string_both_ends('f'))            