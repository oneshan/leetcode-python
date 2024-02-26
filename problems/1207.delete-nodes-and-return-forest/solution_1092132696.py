# 1207 - Delete Nodes And Return Forest
# Date: 2023-11-05
# Runtime: 62 ms, Memory: 16.9 MB
# Submission Id: 1092132696


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        ans = []
        
        def dfs(node, has_parent):
            nonlocal ans
            
            if not node:
                return None
            
            if node.val in to_delete:
                dfs(node.left, False)
                dfs(node.right, False)
                return None
            
            if not has_parent:
                ans.append(node)
                
            node.left = dfs(node.left, True)
            node.right = dfs(node.right, True)
            return node
                
        dfs(root, False)
        return ans