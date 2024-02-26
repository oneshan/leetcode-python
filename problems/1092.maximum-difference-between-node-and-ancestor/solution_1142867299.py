# 1092 - Maximum Difference Between Node and Ancestor
# Date: 2024-01-11
# Runtime: 37 ms, Memory: 19.1 MB
# Submission Id: 1142867299


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, curr_min, curr_max):
            if not node:
                return curr_max - curr_min
            
            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)
            
            return max(traverse(node.left, curr_min, curr_max),
                       traverse(node.right, curr_min, curr_max))
        
        
        return traverse(root, root.val, root.val)