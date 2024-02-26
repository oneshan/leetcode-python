# 0128 - Longest Consecutive Sequence
# Date: 2022-11-03
# Runtime: 531 ms, Memory: 42.2 MB
# Submission Id: 835921247


class DSU:
    def __init__(self, nums):
        self.root = {num: num for num in nums}
        self.rank = {num: 1 for num in nums}
    
    def find(self, num):
        if self.root[num] == num:
            return num
        self.root[num] = self.find(self.root[num])
        return self.root[num]
        
    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        if root_p == root_q:
            return False
        if self.rank[root_p] > self.rank[root_q]:
            self.root[root_q] = root_p
            self.rank[root_p] += self.rank[root_q]
        else:
            self.root[root_p] = root_q
            self.rank[root_q] += self.rank[root_p]
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        dsu = DSU(nums)
        for num in nums:
            if num+1 in nums:
                dsu.union(num, num+1)
        return max(dsu.rank.values())