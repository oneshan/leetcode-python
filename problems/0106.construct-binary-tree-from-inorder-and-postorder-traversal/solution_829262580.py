# 0106 - Construct Binary Tree from Inorder and Postorder Traversal
# Date: 2022-10-24
# Runtime: 67 ms, Memory: 18.8 MB
# Submission Id: 829262580


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pid = len(inorder) - 1
        
        def recur(left, right):
            nonlocal pid
            
            if left > right:
                return None
            
            val = postorder[pid]
            node = TreeNode(val)
            idx = inorder_map[val]
            pid -= 1
            
            node.right = recur(idx+1, right)
            node.left = recur(left, idx-1)
            return node
        
        return recur(0, len(postorder)-1)