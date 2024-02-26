# 2213 - Find All People With Secret
# Date: 2024-02-24
# Runtime: 1738 ms, Memory: 54 MB
# Submission Id: 1184540314


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
    
    def reset(self, x):
        self.root[x] = x


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # O(N)
        uf = UnionFind(n)
        uf.union(0, firstPerson)

        # O(MlogM)
        meetings.sort(key=lambda x: x[2])

        # O(M)
        same_time_meetings = defaultdict(list)
        for a, b, time in meetings:
            same_time_meetings[time].append([a, b])

        # O(M)
        for t in same_time_meetings:
            for a, b in same_time_meetings[t]:
                uf.union(a, b)
            for a, b in same_time_meetings[t]:
                if uf.find(a) != uf.find(0):
                    uf.reset(a)
                    uf.reset(b)
        
        # O(N)
        return [i for i in range(n) if uf.find(i) == uf.find(0)]
