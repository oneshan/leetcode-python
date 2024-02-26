# 2213 - Find All People With Secret
# Date: 2024-02-24
# Runtime: 1650 ms, Memory: 53.2 MB
# Submission Id: 1184536673


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
        uf = UnionFind(n)
        uf.union(0, firstPerson)

        time_bucket = defaultdict(list)
        for a, b, time in meetings:
            time_bucket[time].append([a, b])

        for t in sorted(time_bucket.keys()):
            for a, b in time_bucket[t]:
                uf.union(a, b)
            root = uf.find(0)
            for a, b in time_bucket[t]:
                if uf.find(a) != root:
                    uf.reset(a)
                    uf.reset(b)
        
        root = uf.find(0)
        return [i for i in range(n) if uf.find(i) == root]
