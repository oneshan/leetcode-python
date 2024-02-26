# 1207 - Delete Nodes And Return Forest
# Date: 2023-11-06
# Runtime: 67 ms, Memory: 16.9 MB
# Submission Id: 1092135004


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

            dfs(node.left, node.val not in to_delete)
            dfs(node.right, node.val not in to_delete)
            
            if node.val in to_delete:
                return            
            if not has_parent:
                ans.append(node)
                
            if node.left and node.left.val in to_delete:
                node.left = None
            if node.right and node.right.val in to_delete:
                node.right = None
                
        dfs(root, False)
        return ans