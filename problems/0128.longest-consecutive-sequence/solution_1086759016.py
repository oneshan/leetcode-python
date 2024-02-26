# 0128 - Longest Consecutive Sequence
# Date: 2023-10-29
# Runtime: 556 ms, Memory: 44.1 MB
# Submission Id: 1086759016


class UnionFind:
    def __init__(self, nums):
        self.root = {num: num for num in nums}
        self.rank = {num: 1 for num in nums}
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
            self.rank[rx] += self.rank[ry]
        else:
            self.root[rx] = ry
            self.rank[ry] += self.rank[rx]       

            
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        dsu = UnionFind(nums)
        for num in nums:
            if num + 1 in nums:
                dsu.union(num, num+1)
        return max(dsu.rank.values())