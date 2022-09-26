
def isValid(s: str) -> bool:
    stack = []
    for Paren in s:
        if Paren == '(' or Paren == '{' or Paren == '[':
            stack.append(Paren)
        elif Paren == ')' or Paren == '}' or Paren == ']':
            if stack:
                leftParen = stack.pop()
                if (leftParen == '(' and Paren == ')') or (leftParen == '{' and Paren == '}') or (leftParen == '[' and Paren == ']'):
                    validity = True
                else:
                    return False
            else: 
                return False
    if stack:
        return False
    return validity
print(isValid(r"[((){})]"))