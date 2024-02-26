# 0250 - Count Univalue Subtrees
# Date: 2022-10-23
# Runtime: 51 ms, Memory: 14.2 MB
# Submission Id: 828531190


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def recur(node):
            nonlocal ans
            
            if not node:
                return None
            
            left = recur(node.left)
            right = recur(node.right)
            if left is None:
                left = node.val
            if right is None:
                right = node.val
            
            if node.val == left == right:
                ans += 1
                return node.val
            return 1001
        
        recur(root)
        return ans