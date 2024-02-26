# 0764 - N-ary Tree Level Order Traversal
# Date: 2022-10-22
# Runtime: 92 ms, Memory: 15.9 MB
# Submission Id: 827935915


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            level = []
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            ans.append(level)
        return ans