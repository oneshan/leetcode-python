# 0530 - Minimum Absolute Difference in BST
# Date: 2022-10-03
# Runtime: 117 ms, Memory: 16 MB
# Submission Id: 814283598


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return self.inorder(root, float('-inf'), float('inf'))
    
    def inorder(self, node, low, high):
        if not node:
            return high - low
        left = self.inorder(node.left, low, node.val)
        right = self.inorder(node.right, node.val, high)
        return min(left, right)