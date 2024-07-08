# 0653 - Two Sum IV - Input is a BST
# Date: 2024-06-09
# Runtime: 69 ms, Memory: 20.5 MB
# Submission Id: 1282569657


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inorder(root):
            if not root:
                return
            yield from inorder(root.left)
            yield root.val
            yield from inorder(root.right)
        
        def inorder_rev(root):
            if not root:
                return
            yield from inorder_rev(root.right)
            yield root.val
            yield from inorder_rev(root.left)

        inorder_generator = inorder(root)
        inorder_rev_generator = inorder_rev(root)

        left, right = next(inorder_generator), next(inorder_rev_generator)
        while left < right:
            two_sum = left + right
            if two_sum == k:
                return True
            if two_sum < k:
                left = next(inorder_generator)
            else:
                right = next(inorder_rev_generator)

        return False