# 0133 - Clone Graph
# Date: 2024-05-20
# Runtime: 35 ms, Memory: 16.9 MB
# Submission Id: 1262847585


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        clone = {}

        def dfs(node):
            if not node:
                return None
            if node in clone:
                return clone[node]
                
            clone[node] = Node(node.val)
            for neighbor in node.neighbors:
                clone[node].neighbors.append(dfs(neighbor))
            return clone[node]

        return dfs(node)