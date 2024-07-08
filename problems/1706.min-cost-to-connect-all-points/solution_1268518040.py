# 1706 - Min Cost to Connect All Points
# Date: 2024-05-26
# Runtime: 649 ms, Memory: 84.2 MB
# Submission Id: 1268518040


class UnionFind:
    def __init__(self, size):
        self.groups = size
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] != x:
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_cost(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        n = len(points)
        heap = []
        for i in range(n):
            for j in range(i+1, n):
                cost = get_cost(points[i], points[j])
                heap.append((cost, i, j))
        heapq.heapify(heap)

        uf = UnionFind(n)
        ans = 0
        while heap:
            cost, p1, p2 = heapq.heappop(heap)
            if uf.union(p1, p2):
                ans += cost
            if uf.groups == 1:
                break
        return ans