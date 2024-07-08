# 0772 - Construct Quad Tree
# Date: 2024-06-17
# Runtime: 100 ms, Memory: 17.5 MB
# Submission Id: 1291259359


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
        
        def build(r, c, size):

            if size == 1:
                return Node(grid[r][c], True)

            half_size = size >> 1
            top_left = build(r, c, half_size)
            top_right = build(r, c+half_size, half_size)
            bottom_left = build(r+half_size, c, half_size)
            bottom_right = build(r+half_size, c+half_size, half_size)

            if (
                top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf
                and top_left.val == top_right.val == bottom_left.val == bottom_right.val
            ):
                return top_left

            return Node(grid[r][c], False, top_left, top_right, bottom_left, bottom_right)

        return build(0, 0, len(grid))