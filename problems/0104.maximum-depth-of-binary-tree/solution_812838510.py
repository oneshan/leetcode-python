# 0104 - Maximum Depth of Binary Tree
# Date: 2022-10-02
# Runtime: 101 ms, Memory: 15.4 MB
# Submission Id: 812838510


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            curr_nodes = len(queue)
            for _ in range(curr_nodes):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return depth