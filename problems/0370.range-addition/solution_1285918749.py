# 0370 - Range Addition
# Date: 2024-06-12
# Runtime: 616 ms, Memory: 29 MB
# Submission Id: 1285918749


class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * size * 4
        self.lazy = [0] * size * 4

    def update(self, left, right, idx, query_s, query_e, val):

        if self.lazy[idx]:
            self.tree[idx] += (right-left+1) * self.lazy[idx]
            if left != right:
                self.lazy[2 * idx + 1] += self.lazy[idx]
                self.lazy[2 * idx + 2] += self.lazy[idx]
            self.lazy[idx] = 0

        if left > query_e or right < query_s:
            return 0

        if query_s <= left and right <= query_e:
            self.tree[idx] += (right - left + 1) * val
            if left != right:
                self.lazy[2 * idx + 1] += val
                self.lazy[2 * idx + 2] += val
            return
        
        mid = (left + right) // 2
        self.update(left, mid, 2 * idx + 1, query_s, query_e, val)
        self.update(mid+1, right, 2 * idx + 2, query_s, query_e, val)
        self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2*idx+2]

    def query(self, left, right, idx, query_s, query_e):
        if self.lazy[idx]:
            self.tree[idx] += (right-left+1) * self.lazy[idx]
            if left != right:
                self.lazy[2 * idx + 1] += self.lazy[idx]
                self.lazy[2 * idx + 2] += self.lazy[idx]
            self.lazy[idx] = 0

        if left > query_e or right < query_s:
            return 0

        if query_s <= left and right <= query_e:
            return self.tree[idx]

        mid = (left + right) // 2
        return self.query(left, mid, 2*idx+1, query_s, query_e) + self.query(mid+1, right, 2*idx+2, query_s, query_e)

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        tree = SegmentTree(length)
        for query_s, query_e, val in updates:
            tree.update(0, length-1, 0, query_s, query_e, val)
        
        ans = [0] * length
        for i in range(length):
            ans[i] = tree.query(0, length-1, 0, i, i)
        return ans