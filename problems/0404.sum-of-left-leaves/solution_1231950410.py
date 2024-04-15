# 0404 - Sum of Left Leaves
# Date: 2024-04-14
# Runtime: 34 ms, Memory: 16.7 MB
# Submission Id: 1231950410


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def recur(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if is_left else 0
            return recur(node.left, True) + recur(node.right, False)

        return recur(root, False)