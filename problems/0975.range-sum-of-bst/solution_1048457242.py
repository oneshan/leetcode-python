# 0975 - Range Sum of BST
# Date: 2023-09-13
# Runtime: 161 ms, Memory: 25.1 MB
# Submission Id: 1048457242


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        ans = 0
        
        def recur(node):
            nonlocal ans
            if not node:
                return
            if low <= node.val <= high:
                ans += node.val
            if low < node.val:
                recur(node.left)
            if node.val < high:
                recur(node.right)
        
        recur(root)
        return ans