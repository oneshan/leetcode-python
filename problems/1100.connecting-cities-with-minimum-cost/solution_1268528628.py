# 1100 - Connecting Cities With Minimum Cost
# Date: 2024-05-26
# Runtime: 484 ms, Memory: 23.2 MB
# Submission Id: 1268528628


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size
        self.groups = size
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] >= self.rank[ry]:
            self.root[ry] = rx
            self.rank[rx] += self.rank[ry]
        else:
            self.root[rx] = ry
            self.rank[ry] += self.rank[rx]
        self.groups -= 1
        return True

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)

        heap = []
        for a, b, cost in connections:
            heap.append((cost, a-1, b-1))
        heapq.heapify(heap)
        
        ans = 0
        while heap:
            cost, a, b = heapq.heappop(heap)
            if uf.union(a, b):
                ans += cost
                if uf.groups == 1:
                    return ans
        return -1