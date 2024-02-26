# 0772 - Construct Quad Tree
# Date: 2023-02-27
# Runtime: 104 ms, Memory: 14.8 MB
# Submission Id: 905907980


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
        def is_same_value(x, y, side_len):
            for r in range(x, x+side_len):
                for c in range(y, y+side_len):
                    if grid[r][c] != grid[x][y]:
                        return False
            return True
        
        def build(x, y, side_len):
            if is_same_value(x, y, side_len):
                return Node(grid[x][y], True)
            root = Node(0, False)
            new_side_len = side_len >> 1
            root.topLeft = build(x, y, new_side_len)
            root.topRight = build(x, y+new_side_len, new_side_len)
            root.bottomLeft = build(x+new_side_len, y, new_side_len)
            root.bottomRight = build(x+new_side_len, y+new_side_len, new_side_len)
            return root
        
        return build(0, 0, len(grid))