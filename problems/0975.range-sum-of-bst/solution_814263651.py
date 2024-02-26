# 0975 - Range Sum of BST
# Date: 2022-10-03
# Runtime: 347 ms, Memory: 23 MB
# Submission Id: 814263651


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        _sum = 0
        def traverse(node):
            nonlocal _sum
            if not node:
                return
            if low <= node.val <= high:
                _sum += node.val
            if node.val > low:
                traverse(node.left)
            if node.val < high:
                traverse(node.right)
        traverse(root)
        return _sum