# 2827 - Greatest Common Divisor Traversal
# Date: 2024-02-25
# Runtime: 951 ms, Memory: 31.6 MB
# Submission Id: 1185498662


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
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        m = max(nums) + 1
        n = len(nums)
        if n == 1:
            return True

        dsu = UnionFind(m)
        sieve = [0] * m
        for i in range(2, m):
            if sieve[i] == 0:
                for j in range(i, m, i):
                    sieve[j] = i

        for i in range(n):
            if nums[i] == 1:
                return False
            temp = nums[i]
            while temp > 1:
                factor = sieve[temp]
                temp //= factor
                dsu.union(nums[i], factor)

        root = dsu.find(nums[0])
        for num in nums:
            if dsu.find(num) != root:
                return False
        return True