# 0572 - Subtree of Another Tree
# Date: 2024-05-13
# Runtime: 74 ms, Memory: 16.6 MB
# Submission Id: 1256914216


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def is_same(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r.val != s.val:
                return False
            return is_same(r.left, s.left) and is_same(r.right, s.right)

        stack = [root]
        while stack:
            node = stack.pop()
            if is_same(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False