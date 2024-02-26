# 1116 - Maximum Level Sum of a Binary Tree
# Date: 2023-06-15
# Runtime: 307 ms, Memory: 21.2 MB
# Submission Id: 971483263


from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = defaultdict(int)
        
        def traverse(node, level):
            if not node:
                return
            traverse(node.left, level+1)
            traverse(node.right, level+1)
            level_sum[level] += node.val
            
        traverse(root, 1)
        ans, max_sum = 0, float('-inf')
        for level, val in level_sum.items():
            if val >= max_sum:
                ans, max_sum = level, val
        return ans