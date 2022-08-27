def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    n = str(x)
    rev = n[::-1]
    if rev == n:
        return True
    return False
