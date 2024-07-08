# 0307 - Range Sum Query - Mutable
# Date: 2024-06-12
# Runtime: 1614 ms, Memory: 35.1 MB
# Submission Id: 1285906954


class SegmentTree:

    def __init__(self, nums):
        self.size = len(nums)
        self.tree = [0] * 4 * self.size
        self.build(nums, 0, self.size-1, 0)

    def build(self, nums, left, right, idx):
        if left == right:
            self.tree[idx] = nums[left]
            return
        mid = (left + right) // 2
        self.build(nums, left, mid, 2*idx+1)
        self.build(nums, mid+1, right, 2*idx+2)
        self.tree[idx] = self.tree[2*idx+1] + self.tree[2*idx+2]

    def update(self, left, right, idx, pos, val):

        if left == right:
            self.tree[idx] = val
            return

        mid = (left + right) // 2
        if pos <= mid:
            self.update(left, mid, 2*idx+1, pos, val)
        else:
            self.update(mid+1, right, 2*idx+2, pos, val)

        self.tree[idx] = self.tree[2*idx+1] + self.tree[2*idx+2]        

    def query(self, left, right, idx, query_s, query_e):
        if query_e < left or query_s > right:
            return 0

        if left >= query_s and query_e >= right:
            return self.tree[idx]

        mid = (left + right) // 2
        return self.query(left, mid, 2*idx+1, query_s, query_e) + self.query(mid+1, right, 2*idx+2, query_s, query_e)
        

class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)
        self.size = len(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(0, self.size-1, 0, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(0, self.size-1, 0, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)