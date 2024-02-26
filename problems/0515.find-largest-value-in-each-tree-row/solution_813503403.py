# 0515 - Find Largest Value in Each Tree Row
# Date: 2022-10-02
# Runtime: 130 ms, Memory: 16.6 MB
# Submission Id: 813503403


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        while queue:
            level_nodes = len(queue)
            level_max = float('-inf')
            for _ in range(level_nodes):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(level_max)
        return ans