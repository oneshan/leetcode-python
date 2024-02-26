# 0129 - Sum Root to Leaf Numbers
# Date: 2022-12-06
# Runtime: 37 ms, Memory: 13.9 MB
# Submission Id: 855461713


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return 0
        
        def traverse(node, prev_sum):
            nonlocal ans
            if not node.left and not node.right:
                ans += prev_sum * 10 + node.val
                return
            if node.left:
                traverse(node.left, 10 * prev_sum + node.val)
            if node.right:
                traverse(node.right, 10* prev_sum + node.val)
        
        traverse(root, 0)
        return ans