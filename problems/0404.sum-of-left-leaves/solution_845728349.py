# 0404 - Sum of Left Leaves
# Date: 2022-11-18
# Runtime: 63 ms, Memory: 14.9 MB
# Submission Id: 845728349


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def recursion(node, is_left):
            if not node.left and not node.right:
                return node.val if is_left else 0
            total = 0
            if node.left:
                total += recursion(node.left, True)
            if node.right:
                total += recursion(node.right, False)
            return total
        
        return recursion(root, False)