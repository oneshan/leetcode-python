# 2416 - Evaluate Boolean Binary Tree
# Date: 2024-05-16
# Runtime: 40 ms, Memory: 16.9 MB
# Submission Id: 1259265513


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        TRUE, FALSE, OR, AND = 1, 0, 2, 3

        def recur(root):
            if root.val in (TRUE, FALSE):
                return root.val

            left = recur(root.left)
            right = recur(root.right)
            if root.val == AND:
                return left and right
            if root.val == OR:
                return left or right

        return recur(root)