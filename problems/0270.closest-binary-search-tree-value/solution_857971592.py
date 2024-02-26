# 0270 - Closest Binary Search Tree Value
# Date: 2022-12-11
# Runtime: 82 ms, Memory: 16.1 MB
# Submission Id: 857971592


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.ans = root.val
        
        def dfs(node):
            if not node:
                return
            if abs(node.val - target) < abs(self.ans - target):
                self.ans = node.val
            if node.val > target:
                dfs(node.left)
            if node.val < target:
                dfs(node.right)
                
        dfs(root)
        return self.ans