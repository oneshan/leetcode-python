# 0404 - Sum of Left Leaves
# Date: 2022-11-18
# Runtime: 69 ms, Memory: 14.8 MB
# Submission Id: 845728784


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def recursion(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if is_left else 0
            return recursion(node.left, True) + recursion(node.right, False)
        
        return recursion(root, False)