# 0098 - Validate Binary Search Tree
# Date: 2022-07-17
# Runtime: 81 ms, Memory: 16.3 MB
# Submission Id: 749264454


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, min_v, max_v = stack.pop()
            if node.val < min_v or node.val > max_v:
                return False
            if node.left:
                stack.append((node.left, min_v, node.val-1))
            if node.right:
                stack.append((node.right, node.val+1, max_v))
        return True