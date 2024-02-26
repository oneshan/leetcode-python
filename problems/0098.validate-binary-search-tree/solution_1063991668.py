# 0098 - Validate Binary Search Tree
# Date: 2023-10-01
# Runtime: 49 ms, Memory: 19 MB
# Submission Id: 1063991668


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev = float('-inf')
        
        def inorder(node):
            if not node:
                return True
            
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
                        
        return inorder(root)