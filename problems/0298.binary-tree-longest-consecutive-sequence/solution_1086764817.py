# 0298 - Binary Tree Longest Consecutive Sequence
# Date: 2023-10-29
# Runtime: 69 ms, Memory: 23.7 MB
# Submission Id: 1086764817


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def recur(node, prev_val, length):
            if not node:
                return 0
            
            length = length + 1 if node.val == prev_val + 1 else 1
            return max(
                length,
                recur(node.left, node.val, length),
                recur(node.right, node.val, length),
            )
        
        return recur(root, root.val-1, 0)