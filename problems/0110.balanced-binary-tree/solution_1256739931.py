# 0110 - Balanced Binary Tree
# Date: 2024-05-13
# Runtime: 36 ms, Memory: 17.6 MB
# Submission Id: 1256739931


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        def recur(node):
            if not node:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            if abs(left-right) > 1:
                self.ans = False
            return 1 + max(left, right)

        recur(root)
        return self.ans