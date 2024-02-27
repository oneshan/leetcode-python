# 0543 - Diameter of Binary Tree
# Date: 2024-02-27
# Runtime: 40 ms, Memory: 17.7 MB
# Submission Id: 1187443371


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def recur(node):
            if not node:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        recur(root)
        return self.ans