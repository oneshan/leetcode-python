# 0764 - N-ary Tree Level Order Traversal
# Date: 2022-10-22
# Runtime: 130 ms, Memory: 15.9 MB
# Submission Id: 827934661


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
            curr = []
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                curr.append(node.val)
                if not node.children:
                    continue
                for neighbor in node.children:
                    queue.append(neighbor)
            ans.append(curr)
        return ans