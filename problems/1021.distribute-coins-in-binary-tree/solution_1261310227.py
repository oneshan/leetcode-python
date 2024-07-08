# 1021 - Distribute Coins in Binary Tree
# Date: 2024-05-18
# Runtime: 46 ms, Memory: 16.6 MB
# Submission Id: 1261310227


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
            extra_coins = node.val + left + right - 1
            self.ans += abs(extra_coins)
            return extra_coins
        
        recur(root)
        return self.ans