# 2545 - Height of Binary Tree After Subtree Removal Queries
# Date: 2023-09-18
# Runtime: 1125 ms, Memory: 102.8 MB
# Submission Id: 1051922924


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
                
        @cache
        def get_height(node):
            if not node:
                return -1
            left = get_height(node.left)
            right = get_height(node.right)
            return 1 + max(left, right)
        
        def dfs(node, depth, max_height):
            if not node:
                return
            ans[node.val] = max_height
            dfs(node.left, depth + 1, max(max_height, depth + 1 + get_height(node.right)))
            dfs(node.right, depth + 1, max(max_height, depth + 1 + get_height(node.left)))
        
        ans = defaultdict(int)
        dfs(root, 0, 0)
        return [ans[v] for v in queries]
