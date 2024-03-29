# 0098 - Validate Binary Search Tree
# Date: 2023-09-15
# Runtime: 48 ms, Memory: 18.8 MB
# Submission Id: 1050214495


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = []
        prev, curr = None, root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and prev.val >= curr.val:
                return False
            prev, curr = curr, curr.right
        return True