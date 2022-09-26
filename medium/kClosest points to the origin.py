from heapq import heappop, heappush


def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap , arr = [], []
        for i in points:
            dist = i[0]**2 + i[1]**2
            heappush(heap, (dist, i))
        while k != 0:
            arr.append(heappop(heap)[1])
            k-=1
        return arr