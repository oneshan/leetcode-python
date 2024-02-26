# 0098 - Validate Binary Search Tree
# Date: 2022-10-03
# Runtime: 94 ms, Memory: 16.5 MB
# Submission Id: 814309545


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev >= curr.val:
                return False
            prev = curr.val
            curr = curr.right
        return True