# 0101 - Symmetric Tree
# Date: 2022-10-23
# Runtime: 76 ms, Memory: 13.9 MB
# Submission Id: 828496614


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return check(left.right, right.left) and check(left.left, right.right)

        if not root:
            return True
        return check(root.left, root.right)