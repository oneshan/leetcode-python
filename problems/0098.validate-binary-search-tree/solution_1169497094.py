# 0098 - Validate Binary Search Tree
# Date: 2024-02-08
# Runtime: 42 ms, Memory: 18.3 MB
# Submission Id: 1169497094


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
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            root = stack.pop()
            if prev >= root.val:
                return False
            prev = root.val
            root = root.right
        return True