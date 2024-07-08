# 0307 - Range Sum Query - Mutable
# Date: 2024-06-11
# Runtime: 2385 ms, Memory: 48.4 MB
# Submission Id: 1284354635


class Node:
    def __init__(self, lx, rx):
        self.start = lx
        self.end = rx
        self.left = None
        self.right = None
        self.total = 0
    
class SegmentTree:

    def __init__(self):
        self.root = Node(0, 30000)

    def update(self, node, val, index):
        # Non overlap
        if index < node.start or index > node.end:
            return
        
        # Full overlap
        if index == node.start == node.end:
            node.total = val
            node.left = node.right = None
            return
        
        # Partial overlap
        if not node.left:
            mid = (node.start + node.end) // 2
            node.left = Node(node.start, mid)
            node.right = Node(mid+1, node.end)
        self.update(node.left, val, index)
        self.update(node.right, val, index)
        node.total = node.left.total + node.right.total

    def query(self, node, query_s, query_e):
        if query_e < node.start or node.end < query_s:
            return 0
        if not node.left or (query_s <= node.start and node.end <= query_e):
            return node.total
        return self.query(node.left, query_s, query_e) + self.query(node.right, query_s, query_e)
        

class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree()
        for idx, num in enumerate(nums):
            self.update(idx, num)

    def update(self, index: int, val: int) -> None:
        self.tree.update(self.tree.root, val, index)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(self.tree.root, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)