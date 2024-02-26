# 1465 - Maximum Product of Splitted Binary Tree
# Date: 2022-12-10
# Runtime: 314 ms, Memory: 77.6 MB
# Submission Id: 857362062


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9+7
        subtree_sums = set()
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            _sum = (node.val + left + right)
            subtree_sums.add(_sum)
            return _sum
        
        ans = 0
        total = dfs(root)
        for sub_sum in subtree_sums:
            ans = max(ans, (total - sub_sum) * sub_sum)     
        return ans % MOD