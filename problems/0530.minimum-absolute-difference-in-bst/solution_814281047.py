# 0530 - Minimum Absolute Difference in BST
# Date: 2022-10-03
# Runtime: 66 ms, Memory: 16.2 MB
# Submission Id: 814281047


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
            nonlocal prev, ans
            if not node:
                return
            
            if node.left: inorder(node.left)
            
            if prev is not None:
                ans = min(ans, node.val - prev)
            prev = node.val
            
            if node.right: inorder(node.right)
        
        inorder(root)
        return ans