# 0998 - Check Completeness of a Binary Tree
# Date: 2023-03-15
# Runtime: 45 ms, Memory: 13.9 MB
# Submission Id: 915533733


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        max_idx = count = 0
        
        def dfs(node, idx):
            nonlocal count, max_idx
            if not node:
                return
            count += 1
            max_idx = max(max_idx, idx)
            dfs(node.left, idx*2 + 1)
            dfs(node.right, idx*2 + 2)
        
        dfs(root, 0)
        return max_idx == count - 1