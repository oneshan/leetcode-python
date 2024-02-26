# 0098 - Validate Binary Search Tree
# Date: 2023-09-15
# Runtime: 51 ms, Memory: 19.3 MB
# Submission Id: 1050215862


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev = None
        
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            
            if self.prev and self.prev.val >= node.val:
                return False
            self.prev = node
            
            if not inorder(node.right):
                return False
            
            return True
        
        return inorder(root)
            