# 1029 - Vertical Order Traversal of a Binary Tree
# Date: 2023-10-28
# Runtime: 37 ms, Memory: 16.5 MB
# Submission Id: 1086018820


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = defaultdict(list)
        
        queue = deque([(root, 0, 0)])
        min_col = max_col = 0
        while queue:
            node, row, col = queue.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            table[col].append((row, node.val))
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        
        ans = []
        for i in range(min_col, max_col+1):
            ans.append([val for _, val in sorted(table[i])])
        return ans