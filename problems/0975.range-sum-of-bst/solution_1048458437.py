# 0975 - Range Sum of BST
# Date: 2023-09-13
# Runtime: 163 ms, Memory: 25.1 MB
# Submission Id: 1048458437


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
        if high < root.val:
            return self.rangeSumBST(root.left, low, high)
        if low > root.val:
            return self.rangeSumBST(root.right, low, high)
        
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)