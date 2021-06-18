string = '3' * 95
while '333' in string or '999' in string:
    if '999' in string:
        string = string.replace('999', '3', 1)
    else:
        string = string.replace('333', '9', 1)
    print(string)