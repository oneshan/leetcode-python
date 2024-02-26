# 0270 - Closest Binary Search Tree Value
# Date: 2022-12-11
# Runtime: 60 ms, Memory: 16.1 MB
# Submission Id: 857973083


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        
        while root:
            if abs(root.val - target) < abs(ans - target):
                ans = root.val
            if root.val == target:
                break
            elif root.val > target:
                root = root.left
            else:
                root = root.right
                
        return ans