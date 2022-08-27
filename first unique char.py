def firstUniqChar(s: str) -> int:
        freq = dict()
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1

print(firstUniqChar("dddccdbba"))