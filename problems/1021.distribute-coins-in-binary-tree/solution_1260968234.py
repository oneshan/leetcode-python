# 1021 - Distribute Coins in Binary Tree
# Date: 2024-05-18
# Runtime: 40 ms, Memory: 16.5 MB
# Submission Id: 1260968234


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def recur(node):
            if not node:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            self.ans += abs(left) + abs(right)
            return node.val + left + right - 1
        
        recur(root)
        return self.ans