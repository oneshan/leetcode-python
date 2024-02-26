# 0307 - Range Sum Query - Mutable
# Date: 2023-11-21
# Runtime: 2371 ms, Memory: 52 MB
# Submission Id: 1103451403


class TreeNode:
    def __init__(self, lx, rx):
        # [lx,rx] denote the range of the interval of the node
        # sum denotes the sum for the interval represented by the nod
        self.lx = lx  
        self.rx = rx
        self.left = None 
        self.right = None
        self.sum = 0

class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.root = self.build(arr, 0, n-1)

    def build(self, arr, i, j):
        node = TreeNode(i, j)
        if i == j:
            node.sum = arr[i]
            return node
            
        mid = (i + j) // 2
        node.left = self.build(arr, i, mid)
        node.right = self.build(arr, mid+1, j)
        node.sum = node.left.sum + node.right.sum
        return node

    def update(self, index, value, node=None):
        if node is None:
            node = self.root

        if node.lx == node.rx == index:
            node.sum = value
            return node

        mid = (node.lx + node.rx) // 2
        if index <= mid:
            node.left = self.update(index, value, node.left)
            node.sum = node.left.sum + node.right.sum
        else:
            node.right = self.update(index, value, node.right)
            node.sum = node.left.sum + node.right.sum
        return node
        
    def sum_range(self, i, j, node=None):
        if node is None:
            node = self.root
            
        # no overlap
        if j < node.lx or i > node.rx:
            return 0
        
        # total overlap
        if i <= node.lx and j >= node.rx:
            return node.sum
        
        # partial overlap
        return self.sum_range(i, j, node.left) + self.sum_range(i, j, node.right)
    
    
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