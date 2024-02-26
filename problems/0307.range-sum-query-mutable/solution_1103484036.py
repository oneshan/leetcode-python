# 0307 - Range Sum Query - Mutable
# Date: 2023-11-21
# Runtime: 2343 ms, Memory: 35.5 MB
# Submission Id: 1103484036



class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0] * (n*4)
        self.size = n
        self.build(arr, 0, 0, n-1)

    def build(self, arr, idx, i, j):
        if i == j:
            self.tree[idx] = arr[i]
            return
        mid = (i + j) // 2
        self.build(arr, idx*2+1, i, mid)
        self.build(arr, idx*2+2, mid+1, j)
        self.tree[idx] = self.tree[idx*2+1] + self.tree[idx*2+2]

    def update(self, index, value, idx=None, i=None, j=None):
        if idx is None:
            idx, i, j = 0, 0, self.size-1
            
        if i == j:
            self.tree[idx] = value
            return
        
        mid = (i + j) // 2
        if i <= index <= mid:
            self.update(index, value, idx*2+1, i, mid)
        else:
            self.update(index, value, idx*2+2, mid+1, j)
        self.tree[idx] = self.tree[idx*2+1] + self.tree[idx*2+2]
        
    def sum_range(self, left, right, idx=None, i=None, j=None):
        if idx is None:
            idx, i, j = 0, 0, self.size-1
        if left > j or right < i:
            return 0
        if i >= left and j <= right:
            return self.tree[idx]
        mid = (i + j) // 2
        return (
            self.sum_range(left, right, idx*2+1, i, mid)
            + self.sum_range(left, right, idx*2+2, mid+1, j)
        )
    
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sum_range(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)