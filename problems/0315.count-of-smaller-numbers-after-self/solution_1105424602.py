# 0315 - Count of Smaller Numbers After Self
# Date: 2023-11-24
# Runtime: 3358 ms, Memory: 38.5 MB
# Submission Id: 1105424602



class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (n*2)
        self.size = n

    def update(self, index, value):
        index += self.size
        self.tree[index] += value            
        while index > 1:
            self.tree[index>>1] = self.tree[index] + self.tree[index^1]
            index >>= 1
        
    def query_range(self, i, j):
        res = 0
        left = self.size + i
        right = self.size + j
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