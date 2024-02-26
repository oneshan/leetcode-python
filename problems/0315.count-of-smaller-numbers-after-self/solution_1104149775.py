# 0315 - Count of Smaller Numbers After Self
# Date: 2023-11-22
# Runtime: 7099 ms, Memory: 38.2 MB
# Submission Id: 1104149775


class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (n*4)
        self.size = n

    def op(self, a, b):
        return a + b

    def update(self, index, value, idx=None, i=None, j=None):
        if idx is None:
            idx, i, j = 0, 0, self.size-1
            
        if i == j:
            self.tree[idx] += value
            return
        
        mid = (i + j) // 2
        if index <= mid:
            self.update(index, value, idx*2+1, i, mid)
        else:
            self.update(index, value, idx*2+2, mid+1, j)
        self.tree[idx] = self.op(self.tree[idx*2+1], self.tree[idx*2+2])
        
    def query_range(self, left, right, idx=None, i=None, j=None):
        if idx is None:
            idx, i, j = 0, 0, self.size-1
        if left > j or right < i:
            return 0
        if i >= left and j <= right:
            return self.tree[idx]
        mid = (i + j) // 2
        return self.op(
            self.query_range(left, right, idx*2+1, i, mid),
            self.query_range(left, right, idx*2+2, mid+1, j)
        )

    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        offset = 10 ** 4
        tree = SegmentTree(2 * offset +1)
        
        ans = [0] * n
        for i in range(n-1, -1, -1):
            ans[i] = tree.query_range(0, nums[i] + offset - 1)
            tree.update(nums[i] + offset, 1)
        return ans