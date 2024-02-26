# 0133 - Clone Graph
# Date: 2023-04-08
# Runtime: 37 ms, Memory: 14.3 MB
# Submission Id: 930004577


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        stack = [node]
        clone = {node: Node(node.val)}
        while stack:
            curr = stack.pop()
            clone_node = clone[curr]
            for neighbor in curr.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                clone_node.neighbors.append(clone[neighbor])

        return clone[node]