

from heapq import nlargest, heapify, heappop, heappush


def topKFrequent(words: list[str], k) -> list[str]:
    # freq = {}
    # heap = []
    # ans = []
    # for word in words:
    #     if word not in freq:
    #         freq[word] = 1
    #     else:
    #         freq[word] += 1
    # for key in freq.keys():
    #     heappush(heap, key)
    return nlargest(k, words)
print(topKFrequent(["i","love","leetcode","i","love","coding"], 2))