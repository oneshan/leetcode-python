# 1568 - Pseudo-Palindromic Paths in a Binary Tree
# Date: 2024-01-24
# Runtime: 490 ms, Memory: 46.2 MB
# Submission Id: 1155124539


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
        
        def recur(node, counter):
            res = 0
            
            if not node.left and not node.right:
                for i in range(1, 10):
                    if counter[i] & 1:
                        res += 1
                return int(res in (0, 1))
            
            for next_node in (node.left, node.right):
                if next_node:    
                    counter[next_node.val] -= 1
                    res += recur(next_node, counter)
                    counter[next_node.val] -= 1
            return res
        
        counter = [0] * 10
        counter[root.val] += 1
        return recur(root, counter)