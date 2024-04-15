# 0129 - Sum Root to Leaf Numbers
# Date: 2024-04-15
# Runtime: 42 ms, Memory: 16.5 MB
# Submission Id: 1232681637


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def recur(node, val):
            val = val * 10 + node.val
            if not node.left and not node.right:
                self.ans += val
                return
            if node.left:
                recur(node.left, val)
            if node.right:
                recur(node.right, val)

        if not root:
            return 0
        recur(root, 0)
        return self.ans