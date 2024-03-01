# 0124 - Binary Tree Maximum Path Sum
# Date: 2024-02-29
# Runtime: 60 ms, Memory: 20.9 MB
# Submission Id: 1189251748


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def recur(node):
            if not node:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            self.ans = max(self.ans, node.val + left + right)
            return max(0, node.val + left, node.val + right)

        recur(root)
        return self.ans