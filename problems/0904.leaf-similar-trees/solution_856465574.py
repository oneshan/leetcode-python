# 0904 - Leaf-Similar Trees
# Date: 2022-12-08
# Runtime: 83 ms, Memory: 14 MB
# Submission Id: 856465574


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def recur(node, arr):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node.val)
                return
            recur(node.left, arr)
            recur(node.right, arr)
        
        leaf1, leaf2 = [], []
        recur(root1, leaf1)
        recur(root2, leaf2)
        return leaf1 == leaf2