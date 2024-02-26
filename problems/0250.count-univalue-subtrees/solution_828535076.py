# 0250 - Count Univalue Subtrees
# Date: 2022-10-23
# Runtime: 78 ms, Memory: 14 MB
# Submission Id: 828535076


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def recur(node, val):
            nonlocal ans
            
            if not node:
                return True
            
            left = recur(node.left, node.val)
            right = recur(node.right, node.val)
            if not left or not right:
                return False
            
            ans += 1
            return node.val == val
        
        recur(root, 0)
        return ans