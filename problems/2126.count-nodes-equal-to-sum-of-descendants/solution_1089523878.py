# 2126 - Count Nodes Equal to Sum of Descendants
# Date: 2023-11-02
# Runtime: 612 ms, Memory: 138 MB
# Submission Id: 1089523878


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        def recur(node):
            nonlocal ans
            
            if not node:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            if left + right == node.val:
                ans += 1
            return left + right + node.val
        
        ans = 0
        recur(root)
        return ans