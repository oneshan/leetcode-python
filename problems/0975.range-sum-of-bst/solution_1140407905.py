# 0975 - Range Sum of BST
# Date: 2024-01-08
# Runtime: 117 ms, Memory: 24.4 MB
# Submission Id: 1140407905


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        res = 0
        if low <= root.val <= high:
            res += root.val
        if root.val >= low:
            res += self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            res += self.rangeSumBST(root.right, low, high)
        
        return res 