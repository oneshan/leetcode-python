# 0235 - Lowest Common Ancestor of a Binary Search Tree
# Date: 2022-07-17
# Runtime: 164 ms, Memory: 18.9 MB
# Submission Id: 749435138


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val = p.val, q.val
        while root:
            curr = root.val
            if p_val < curr and q_val < curr:
                root = root.left
            elif p_val > curr and q_val > curr:
                root = root.right
            else:
                return root
        return None
        