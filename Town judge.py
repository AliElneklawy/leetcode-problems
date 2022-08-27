from collections import defaultdict


def findJudge(n: int, trust: list[list[int]]) -> int:
        target = -1
        d = defaultdict(list)
        for i in trust:
            d[i[0]].append(i[1]) 
        while n > 0:
            if n not in d:
                target = n
                break
            n-=1
        for possibleJudge in d.values():
            if target not in possibleJudge: return -1
        return target
print(findJudge(4, [[1,3],[1,4],[2,3]]))