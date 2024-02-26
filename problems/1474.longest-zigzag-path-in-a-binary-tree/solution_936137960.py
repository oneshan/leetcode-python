# 1474 - Longest ZigZag Path in a Binary Tree
# Date: 2023-04-19
# Runtime: 371 ms, Memory: 61.4 MB
# Submission Id: 936137960


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def recur(node, left, right):
            if not node:
                return
            
            self.ans = max(self.ans, left, right)
            if node.left:
                recur(node.left, right+1, 0)
            if node.right:
                recur(node.right, 0, left+1)

        recur(root, 0, 0)
        return self.ans