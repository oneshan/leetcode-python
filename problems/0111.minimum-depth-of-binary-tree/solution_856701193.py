# 0111 - Minimum Depth of Binary Tree
# Date: 2022-12-08
# Runtime: 1369 ms, Memory: 49.5 MB
# Submission Id: 856701193


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
                if not node.left and not node.right:
                    return depth
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)