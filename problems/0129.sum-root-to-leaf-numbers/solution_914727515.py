# 0129 - Sum Root to Leaf Numbers
# Date: 2023-03-14
# Runtime: 36 ms, Memory: 13.8 MB
# Submission Id: 914727515


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        
        def traverse(node, prev_sum):
            nonlocal ans
            curr_val = prev_sum * 10 + node.val
            if not node.left and not node.right:
                ans += curr_val
                return
            if node.left:
                traverse(node.left, curr_val)
            if node.right:
                traverse(node.right, curr_val)
                
        traverse(root, 0)
        return ans