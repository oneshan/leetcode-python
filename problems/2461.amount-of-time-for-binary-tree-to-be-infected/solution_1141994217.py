# 2461 - Amount of Time for Binary Tree to Be Infected
# Date: 2024-01-10
# Runtime: 255 ms, Memory: 52.9 MB
# Submission Id: 1141994217


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0
        
        def traverse(node):
            nonlocal ans
            
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            if node.val == start:
                ans = max(left, right)
                return -1
            if left < 0 or right < 0:
                ans = max(ans, abs(left) + abs(right))
                return min(left, right) - 1
        
            return 1 + max(left, right)
        
        traverse(root)
        return ans