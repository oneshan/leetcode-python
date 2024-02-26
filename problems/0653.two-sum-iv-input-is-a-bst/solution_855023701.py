# 0653 - Two Sum IV - Input is a BST
# Date: 2022-12-05
# Runtime: 214 ms, Memory: 20 MB
# Submission Id: 855023701


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
        
        inorder_gen = inorder(root)
        inorder_rev_gen = inorder_rev(root)
        
        left, right = next(inorder_gen), next(inorder_rev_gen)
        while left < right:
            two_sum = left + right
            if two_sum == k:
                return True
            if two_sum < k:
                left = next(inorder_gen)
            else:
                right = next(inorder_rev_gen)
        return False