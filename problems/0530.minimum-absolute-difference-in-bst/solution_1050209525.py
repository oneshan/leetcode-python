# 0530 - Minimum Absolute Difference in BST
# Date: 2023-09-15
# Runtime: 58 ms, Memory: 18.7 MB
# Submission Id: 1050209525


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        prev = None
        
        def inorder(node):
            nonlocal ans, prev
            
            if not node:
                return
            inorder(node.left)
            if prev:
                ans = min(ans, abs(node.val - prev.val))
            prev = node
            inorder(node.right)
        
        inorder(root)
        return ans