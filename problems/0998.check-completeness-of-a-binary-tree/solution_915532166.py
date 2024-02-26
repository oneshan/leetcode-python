# 0998 - Check Completeness of a Binary Tree
# Date: 2023-03-15
# Runtime: 33 ms, Memory: 13.9 MB
# Submission Id: 915532166


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
        
        queue = deque([(root, 0)])
        prev_idx = -1
        while queue:
            node, idx = queue.popleft()
            if idx > prev_idx + 1:
                return False
            if node.left:
                queue.append((node.left, idx*2 + 1))
            if node.right:
                queue.append((node.right, idx*2 + 2))
            prev_idx = idx
        return True