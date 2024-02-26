# 0307 - Range Sum Query - Mutable
# Date: 2023-11-24
# Runtime: 1593 ms, Memory: 34.5 MB
# Submission Id: 1105429549


class SegmentTree:
    def __init__(self, nums):
        self.size = len(nums)
        self.tree = [0] * self.size + nums
        for i in range(self.size-1, -1, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
        
    def update(self, index, value):
        index += self.size
        self.tree[index] = value            
        while index > 1:
            self.tree[index>>1] = self.tree[index] + self.tree[index^1]
            index >>= 1
        
    def query_range(self, i, j):
        res = 0
        left = self.size + i
        right = self.size + j + 1
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
    
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query_range(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)