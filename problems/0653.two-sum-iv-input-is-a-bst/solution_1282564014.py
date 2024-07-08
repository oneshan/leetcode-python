# 0653 - Two Sum IV - Input is a BST
# Date: 2024-06-09
# Runtime: 75 ms, Memory: 18.3 MB
# Submission Id: 1282564014


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def traverse(root, target):
            if not root:
                return False
            if root.val == target:
                return True
            if root.val < target:
                return traverse(root.right, target)
            return traverse(root.left, target)

        stack = [root]
        while stack:
            node = stack.pop()
            if k != node.val * 2 and traverse(root, k-node.val):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False