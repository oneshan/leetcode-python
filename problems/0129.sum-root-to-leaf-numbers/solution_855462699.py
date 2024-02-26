# 0129 - Sum Root to Leaf Numbers
# Date: 2022-12-06
# Runtime: 55 ms, Memory: 13.8 MB
# Submission Id: 855462699


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
            curr_sum = prev_sum * 10 + node.val
            if not node.left and not node.right:
                ans += curr_sum
                return
            if node.left:
                traverse(node.left, curr_sum)
            if node.right:
                traverse(node.right, curr_sum)
        
        traverse(root, 0)
        return ans