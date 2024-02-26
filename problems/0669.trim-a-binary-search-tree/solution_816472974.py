# 0669 - Trim a Binary Search Tree
# Date: 2022-10-06
# Runtime: 113 ms, Memory: 18 MB
# Submission Id: 816472974


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None 
        
        left = self.trimBST(root.left, low, high)
        right = self.trimBST(root.right, low, high)
        if low <= root.val <= high:
            root.left, root.right = left, right
            return root
        return left or right