# 0975 - Range Sum of BST
# Date: 2022-10-03
# Runtime: 222 ms, Memory: 23 MB
# Submission Id: 814271452


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
        left = self.rangeSumBST(root.left, low, high) if root.val >= low else 0
        right = self.rangeSumBST(root.right, low, high) if root.val <= high else 0
        curr = root.val if low <= root.val <= high else 0
        return left + right + curr