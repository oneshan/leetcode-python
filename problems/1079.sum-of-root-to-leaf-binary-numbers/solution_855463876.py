# 1079 - Sum of Root To Leaf Binary Numbers
# Date: 2022-12-06
# Runtime: 81 ms, Memory: 14.1 MB
# Submission Id: 855463876


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def traverse(node, curr_sum):
            nonlocal ans
            curr_sum = (curr_sum << 1) + node.val
            if not node.left and not node.right:
                ans += curr_sum
                return
            if node.left:
                traverse(node.left, curr_sum)
            if node.right:
                traverse(node.right, curr_sum)
        
        traverse(root, 0)
        return ans