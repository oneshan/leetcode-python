# 0098 - Validate Binary Search Tree
# Date: 2022-07-17
# Runtime: 43 ms, Memory: 16.5 MB
# Submission Id: 749261663


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, float('-inf'), float('inf'))
        
    def traverse(self, node, min_v, max_v):
        if not node:
            return True
        if node.val < min_v or node.val > max_v:
            return False
        return (
            self.traverse(node.left, min_v, node.val-1)
            and self.traverse(node.right, node.val+1, max_v)
        )