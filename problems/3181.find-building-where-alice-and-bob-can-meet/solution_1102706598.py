# 3181 - Find Building Where Alice and Bob Can Meet
# Date: 2023-11-20
# Runtime: 2150 ms, Memory: 41.3 MB
# Submission Id: 1102706598



class SegmentTree:

    def __init__(self, n):
        self.tree = [0] * (n * 4)

    def build(self, arr, idx, left, right):
        if left == right:
            self.tree[idx] = arr[left]
            return
        mid = (left + right) // 2
        self.build(arr, idx * 2, left, mid)
        self.build(arr, idx * 2 + 1, mid + 1, right)
        self.tree[idx] = max(self.tree[idx*2], self.tree[idx*2+1])

    def bisect(self, idx, left, right, i, target):
        if self.tree[idx] < target:
            return -1
        if left == right:
            return left
        
        mid = (left + right) // 2
        if i <= mid and self.tree[idx*2] >= target:
            res = self.bisect(idx * 2, left, mid, i, target)
            if res != -1:
                return res
        return self.bisect(idx*2+1, mid+1, right, i, target)

    
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        tree = SegmentTree(n)
        tree.build(heights, 1, 0, n-1)
        
        def get_ans(a, b):
            if a == b:
                return a
            if a > b:
                a, b = b, a
            if heights[a] < heights[b]:
                return b
            
            target = max(heights[a], heights[b]) + 1
            return tree.bisect(1, 0, n-1, b+1, target)
        
        return [get_ans(a, b) for a, b in queries]