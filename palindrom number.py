def isPalindrome(x: int) -> bool:
        return False if x < 0 else str(x) == str(x)[::-1]
