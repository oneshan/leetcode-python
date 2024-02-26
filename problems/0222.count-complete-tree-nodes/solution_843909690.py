# 0222 - Count Complete Tree Nodes
# Date: 2022-11-15
# Runtime: 228 ms, Memory: 21.4 MB
# Submission Id: 843909690


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
        return 1 + self.countNodes(root.right) + self.countNodes(root.left)