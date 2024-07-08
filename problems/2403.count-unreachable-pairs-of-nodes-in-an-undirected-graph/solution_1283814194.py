# 2403 - Count Unreachable Pairs of Nodes in an Undirected Graph
# Date: 2024-06-10
# Runtime: 1639 ms, Memory: 77.5 MB
# Submission Id: 1283814194


class UnionFind:
    def __init__(self, size):
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
        return True

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)

        counter = Counter()
        for i in range(n):
            counter[uf.find(i)] += 1

        ans = 0
        for cnt in counter.values():
            ans += cnt * (n-cnt)
            n -= cnt
        return ans