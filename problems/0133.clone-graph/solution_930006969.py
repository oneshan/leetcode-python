# 0133 - Clone Graph
# Date: 2023-04-08
# Runtime: 47 ms, Memory: 14.4 MB
# Submission Id: 930006969


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clone = {}
        
        def dfs(node):
            if not node:
                return None
            if node in clone:
                return clone[node]
            
            clone[node] = Node(node.val)
            clone[node].neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            return clone[node]
        
        return dfs(node)