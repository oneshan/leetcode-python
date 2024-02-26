# 1207 - Delete Nodes And Return Forest
# Date: 2023-11-06
# Runtime: 63 ms, Memory: 16.8 MB
# Submission Id: 1092136258


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
                return      
            
            if not has_parent:
                ans.append(node)
            
            if node.left:
                dfs(node.left, True)
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                dfs(node.right, True)
                if node.right.val in to_delete:
                    node.right = None
                
        dfs(root, False)
        return ans