# 0606 - Construct String from Binary Tree
# Date: 2023-12-08
# Runtime: 47 ms, Memory: 18.8 MB
# Submission Id: 1114923722


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            if not node:
                return ''
            left = dfs(node.left)
            right = dfs(node.right)
            if right:
                return f'{node.val}({left})({right})'
            elif left:
                return f'{node.val}({left})'                
            return f'{node.val}'
        
        return dfs(root)