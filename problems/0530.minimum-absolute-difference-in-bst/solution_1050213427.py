# 0530 - Minimum Absolute Difference in BST
# Date: 2023-09-15
# Runtime: 60 ms, Memory: 18.6 MB
# Submission Id: 1050213427


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        
        stack = []
        prev, curr = None, root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev:
                ans = min(ans, curr.val - prev.val)
            prev, curr = curr, curr.right
        
        return ans