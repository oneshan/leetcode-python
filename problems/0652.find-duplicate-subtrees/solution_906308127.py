# 0652 - Find Duplicate Subtrees
# Date: 2023-02-28
# Runtime: 46 ms, Memory: 21.2 MB
# Submission Id: 906308127


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        table = defaultdict(int)
        ans = []
        
        def recur(node):
            if not node:
                return ''
            left = recur(node.left)
            right = recur(node.right)
            path = f'L{left}{node.val}{right}R'
            if table[path] == 1:
                ans.append(node)
            table[path] += 1
            return path
        
        recur(root)
        return ans