# 0975 - Range Sum of BST
# Date: 2024-01-08
# Runtime: 105 ms, Memory: 24.5 MB
# Submission Id: 1140408990


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ans += node.val
            if low < node.val and node.left:
                stack.append(node.left)
            if high > node.val and node.right:
                stack.append(node.right)
        return ans