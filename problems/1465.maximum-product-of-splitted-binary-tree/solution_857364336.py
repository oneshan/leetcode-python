# 1465 - Maximum Product of Splitted Binary Tree
# Date: 2022-12-10
# Runtime: 390 ms, Memory: 75.6 MB
# Submission Id: 857364336


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9+7
        
        def dfs(node, total_sum=None):
            if not node:
                return 0
            left = dfs(node.left, total_sum)
            right = dfs(node.right, total_sum)
            subtree_sum = node.val + left + right
            if total_sum:
                self.ans = max(self.ans, subtree_sum * (total_sum - subtree_sum))
            return subtree_sum
        
        self.ans = 0
        total_sum = dfs(root)
        dfs(root, total_sum)
        return self.ans % MOD