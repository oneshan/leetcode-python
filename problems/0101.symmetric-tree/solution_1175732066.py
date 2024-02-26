# 0101 - Symmetric Tree
# Date: 2024-02-15
# Runtime: 36 ms, Memory: 16.6 MB
# Submission Id: 1175732066


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return (
                n1.val == n2.val
                and check(n1.left, n2.right)
                and check(n1.right, n2.left)
            )
        
        if not root:
            return True
        return check(root.left, root.right)