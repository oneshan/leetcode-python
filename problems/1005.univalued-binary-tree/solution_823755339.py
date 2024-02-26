# 1005 - Univalued Binary Tree
# Date: 2022-10-16
# Runtime: 58 ms, Memory: 13.8 MB
# Submission Id: 823755339


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        value = root.val
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val != value:
                return False
            stack.append(node.left)
            stack.append(node.right)
        return True