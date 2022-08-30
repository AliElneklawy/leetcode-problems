from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    freq = Counter(s)
    for char in t:
        if char in freq and t.count(char) == freq[char]:
            valid = True
        else:
            return False
    return valid
print(isAnagram("ab", 'a'))
