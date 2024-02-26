# 0104 - Maximum Depth of Binary Tree
# Date: 2023-02-16
# Runtime: 46 ms, Memory: 15.1 MB
# Submission Id: 898838830


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
            ans = max(ans, depth)
        return ans