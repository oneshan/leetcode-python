# 0098 - Validate Binary Search Tree
# Date: 2023-09-15
# Runtime: 56 ms, Memory: 18.7 MB
# Submission Id: 1050219194


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur(node, curr_min, curr_max):
            if not node:
                return True
            if curr_min < node.val < curr_max:
                return (recur(node.left, curr_min, node.val)
                        and recur(node.right, node.val, curr_max))
            return False
        
        return recur(root, float('-inf'), float('inf'))
                        