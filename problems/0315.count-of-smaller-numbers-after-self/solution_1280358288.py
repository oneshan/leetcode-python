# 0315 - Count of Smaller Numbers After Self
# Date: 2024-06-07
# Runtime: 1272 ms, Memory: 37.9 MB
# Submission Id: 1280358288


class BITTree:
    def __init__(self, offset):
        self.offset = offset
        self.size = 1 + offset * 2
        self.bits = [0] * (1 + self.size)

    def update(self, idx, val):
        idx += 1 + self.offset
        while idx <= self.size:
            self.bits[idx] += val
            idx += idx & -idx
    
    def get_sum(self, idx):
        idx += self.offset
        res = 0
        while idx > 0:
            res += self.bits[idx]
            idx -= idx & -idx
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        offset = 10_000
        tree = BITTree(offset)
        ans = []
        for num in nums[::-1]:
            ans.append(tree.get_sum(num))
            tree.update(num, 1)
        return ans[::-1]