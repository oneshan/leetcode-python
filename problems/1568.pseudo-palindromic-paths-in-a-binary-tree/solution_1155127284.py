# 1568 - Pseudo-Palindromic Paths in a Binary Tree
# Date: 2024-01-24
# Runtime: 351 ms, Memory: 47 MB
# Submission Id: 1155127284


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def recur(node, count):
            res = 0
            
            if not node.left and not node.right:
                return int(count & (count-1) == 0)
            
            for next_node in (node.left, node.right):
                if next_node:    
                    res += recur(next_node, count ^ (1 << next_node.val))
            return res
        
        return recur(root, 1 << root.val)