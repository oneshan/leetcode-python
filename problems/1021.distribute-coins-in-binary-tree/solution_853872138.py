# 1021 - Distribute Coins in Binary Tree
# Date: 2022-12-03
# Runtime: 38 ms, Memory: 13.7 MB
# Submission Id: 853872138


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right= dfs(node.right)
            ans += abs(left) + abs(right)
            return node.val + left + right - 1
        
        ans = 0
        dfs(root)
        return ans