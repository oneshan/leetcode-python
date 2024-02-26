# 0975 - Range Sum of BST
# Date: 2022-12-06
# Runtime: 360 ms, Memory: 23.1 MB
# Submission Id: 855469977


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        
        def traverse(node):
            nonlocal ans
            if low <= node.val <= high:
                ans += node.val
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        
        traverse(root)
        return ans