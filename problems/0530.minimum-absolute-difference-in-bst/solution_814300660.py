# 0530 - Minimum Absolute Difference in BST
# Date: 2022-10-03
# Runtime: 123 ms, Memory: 16.1 MB
# Submission Id: 814300660


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
        curr = root
        prev = None
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev is not None: ans = min(ans, curr.val-prev)
                prev = curr.val
                curr = curr.right
        return ans