# 1254 - Deepest Leaves Sum
# Date: 2022-10-02
# Runtime: 213 ms, Memory: 17.8 MB
# Submission Id: 813509072


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 0)]
        depth = depth_sum = 0
        while stack:
            node, level = stack.pop()
            
            if level > depth:
                depth, depth_sum = level, node.val
            elif level == depth:
                depth_sum += node.val

            if node.left: stack.append((node.left, level+1))
            if node.right: stack.append((node.right, level+1))
            
        return depth_sum