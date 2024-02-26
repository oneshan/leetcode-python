# 0315 - Count of Smaller Numbers After Self
# Date: 2023-11-22
# Runtime: 3382 ms, Memory: 38.7 MB
# Submission Id: 1104154236


class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (n*2)
        self.size = n

    def op(self, a, b):
        return a + b

    def update(self, index, value):
        index += self.size
        self.tree[index] += value
        while index > 1:
            index >>= 1
            self.tree[index] = self.tree[index*2] + self.tree[index*2 + 1]
        
    def query_range(self, left, right):
        res = 0
        left, right = left + self.size, right + self.size
        while left < right:
            if left & 1:
                res += self.tree[left]
                left += 1
            left >>= 1
            if right & 1:
                right -= 1
                res += self.tree[right]
            right >>= 1
        return res
    
    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        offset = 10 ** 4
        tree = SegmentTree(2 * offset +1)
        
        ans = [0] * n
        for i in range(n-1, -1, -1):
            ans[i] = tree.query_range(0, nums[i] + offset)
            tree.update(nums[i] + offset, 1)

        return ans