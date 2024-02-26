# 0783 - Search in a Binary Search Tree
# Date: 2022-10-27
# Runtime: 188 ms, Memory: 16.5 MB
# Submission Id: 831393907


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        return self.searchBST(root.right if root.val < val else root.left, val)