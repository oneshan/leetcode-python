# 1207 - Delete Nodes And Return Forest
# Date: 2022-10-16
# Runtime: 71 ms, Memory: 14.3 MB
# Submission Id: 823591975


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
        
        def traverse(node, parent_exist):
            if not node:
                return None
            if node.val in to_delete:
                traverse(node.left, False)
                traverse(node.right, False)
                return None
            
            if not parent_exist:
                ans.append(node)
                
            node.left = traverse(node.left, True)
            node.right = traverse(node.right, True)
            return node
        
        traverse(root, False)
        return ans