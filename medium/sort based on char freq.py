def frequencySort(s: str) -> str:
    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char]+=1
    return sorted(freq, key=lambda char:freq[char], reverse=True)
    print(freq)

print(frequencySort("tree"))