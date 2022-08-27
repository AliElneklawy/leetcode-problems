def lengthOfLastWord(s: str) -> int:
    s = s.strip().split()
    return len(s[-1])
