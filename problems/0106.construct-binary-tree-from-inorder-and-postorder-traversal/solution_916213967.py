# 0106 - Construct Binary Tree from Inorder and Postorder Traversal
# Date: 2023-03-16
# Runtime: 64 ms, Memory: 18.9 MB
# Submission Id: 916213967


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pid = len(postorder) - 1
        
        def recursion(left, right):
            nonlocal pid
            
            if left > right:
                return None
            
            val = postorder[pid]
            node = TreeNode(val)
            pid -= 1
            
            idx = inorder_map[val]
            node.right = recursion(idx+1, right)
            node.left = recursion(left, idx-1)
            return node
        
        return recursion(0, len(inorder)-1)