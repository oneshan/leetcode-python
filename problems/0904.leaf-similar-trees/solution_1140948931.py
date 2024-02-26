# 0904 - Leaf-Similar Trees
# Date: 2024-01-09
# Runtime: 34 ms, Memory: 17.3 MB
# Submission Id: 1140948931


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(node, arr):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node.val)
            traverse(node.left, arr)
            traverse(node.right, arr)
            
        r1, r2 = [], []
        traverse(root1, r1)
        traverse(root2, r2)
        return r1 == r2