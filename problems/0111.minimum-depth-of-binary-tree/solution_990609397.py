# 0111 - Minimum Depth of Binary Tree
# Date: 2023-07-10
# Runtime: 475 ms, Memory: 51.6 MB
# Submission Id: 990609397


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.right and not node.left:
                    return depth
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)