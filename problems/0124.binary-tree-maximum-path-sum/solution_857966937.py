# 0124 - Binary Tree Maximum Path Sum
# Date: 2022-12-11
# Runtime: 203 ms, Memory: 21.4 MB
# Submission Id: 857966937


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float('-inf')
        
        def get_sum(node):
            if not node:
                return 0
            left = max(get_sum(node.left), 0)
            right = max(get_sum(node.right), 0)
            self.ans = max(self.ans, left+right+node.val)
            return node.val + max(left, right)
        
        get_sum(root)
        return self.ans