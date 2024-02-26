# 0662 - Maximum Width of Binary Tree
# Date: 2023-04-20
# Runtime: 41 ms, Memory: 14.7 MB
# Submission Id: 936632954


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        ans = 0
        while queue:
            prev = None
            for _ in range(len(queue)):
                node, nid = queue.popleft()
                if prev is None:
                    prev = nid
                if node.left:
                    queue.append((node.left, nid*2))
                if node.right:
                    queue.append((node.right, nid*2 + 1))
                ans = max(ans, nid-prev+1)
        return ans