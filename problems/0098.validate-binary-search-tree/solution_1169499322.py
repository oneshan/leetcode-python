# 0098 - Validate Binary Search Tree
# Date: 2024-02-08
# Runtime: 49 ms, Memory: 18.3 MB
# Submission Id: 1169499322


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur(node, min_v, max_v):
            if not node:
                return True
            if node.val < min_v or node.val > max_v:
                return False
            return (
                recur(node.left, min_v, node.val-1)
                and recur(node.right, node.val+1, max_v)
            )
        
        return recur(root, float('-inf'), float('inf'))