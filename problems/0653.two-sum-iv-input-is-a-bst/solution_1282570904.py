# 0653 - Two Sum IV - Input is a BST
# Date: 2024-06-09
# Runtime: 63 ms, Memory: 18.6 MB
# Submission Id: 1282570904


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val in seen:
                return True
            seen.add(k-node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False