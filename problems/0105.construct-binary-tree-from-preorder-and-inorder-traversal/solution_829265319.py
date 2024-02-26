# 0105 - Construct Binary Tree from Preorder and Inorder Traversal
# Date: 2022-10-24
# Runtime: 105 ms, Memory: 18.9 MB
# Submission Id: 829265319


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pid = 0
        
        def recur(left, right):
            nonlocal pid
            if left > right:
                return None
            
            val = preorder[pid]
            idx = inorder_map[val]
            pid += 1
            
            node = TreeNode(val)
            node.left = recur(left, idx-1)
            node.right = recur(idx+1, right)
            return node
        
        return recur(0, len(inorder)-1)