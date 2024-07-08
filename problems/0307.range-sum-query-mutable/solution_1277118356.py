# 0307 - Range Sum Query - Mutable
# Date: 2024-06-04
# Runtime: 1061 ms, Memory: 33.9 MB
# Submission Id: 1277118356


class BITTree:
    def __init__(self, nums):
        self.size = len(nums)
        self.bits = [0] * (len(nums)+1)
        for idx, num in enumerate(nums):
            self.update(idx, num)
    
    def update(self, idx, val):
        idx += 1
        while idx <= self.size:
            self.bits[idx] += val
            idx += idx & -idx

    def get_sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bits[idx]
            idx -= idx & -idx
        return res

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = BITTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.get_sum(right) - self.tree.get_sum(left-1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)