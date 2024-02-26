# 0222 - Count Complete Tree Nodes
# Date: 2023-10-10
# Runtime: 78 ms, Memory: 23.7 MB
# Submission Id: 1071760895


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left, node = 0, root
        while node:
            node = node.left
            left += 1
        
        right, node = 0, root
        while node:
            node = node.right
            right += 1
            
        if left == right:
            return 2 ** left - 1
        return 1 + self.countNodes(root.right) + self.countNodes(root.left)