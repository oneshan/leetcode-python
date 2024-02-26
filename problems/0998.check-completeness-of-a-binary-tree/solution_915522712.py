# 0998 - Check Completeness of a Binary Tree
# Date: 2023-03-15
# Runtime: 32 ms, Memory: 13.8 MB
# Submission Id: 915522712


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
        prev_node = root
        while queue:
            node = queue.popleft()
            if node:
                if not prev_node:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            prev_node = node
        return True