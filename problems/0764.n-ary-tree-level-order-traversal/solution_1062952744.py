# 0764 - N-ary Tree Level Order Traversal
# Date: 2023-09-30
# Runtime: 52 ms, Memory: 18.3 MB
# Submission Id: 1062952744


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

        ans = []
        queue = deque([root])
        while queue:
            ans.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                ans[-1].append(node.val)
                for child in node.children:
                    if child:
                        queue.append(child)
        
        return ans