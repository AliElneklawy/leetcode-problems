def plusOne(digits):
    string = str(int(''.join(map(str, digits)))+1)
    return [*string]

