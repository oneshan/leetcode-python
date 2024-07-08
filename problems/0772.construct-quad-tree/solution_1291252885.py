# 0772 - Construct Quad Tree
# Date: 2024-06-17
# Runtime: 91 ms, Memory: 17.4 MB
# Submission Id: 1291252885


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def is_same(r, c, size):
            for nr in range(r, r+size):
                for nc in range(c, c+size):
                    if grid[r][c] != grid[nr][nc]:
                        return False
            return True

        def build(r, c, size):
            if is_same(r, c, size):
                return Node(grid[r][c], True)

            root = Node(grid[r][c], False)
            half_size = size >> 1
            root.topLeft = build(r, c, half_size)
            root.topRight = build(r, c+half_size, half_size)
            root.bottomLeft = build(r+half_size, c, half_size)
            root.bottomRight = build(r+half_size, c+half_size, half_size)
            return root

        return build(0, 0, len(grid))