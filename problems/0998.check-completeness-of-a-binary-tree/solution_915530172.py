# 0998 - Check Completeness of a Binary Tree
# Date: 2023-03-15
# Runtime: 35 ms, Memory: 13.8 MB
# Submission Id: 915530172


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
        
        queue = deque([root])
        prev_null = False
        while queue:
            node = queue.popleft()
            if not node:
                prev_null = True
            else:
                if prev_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True