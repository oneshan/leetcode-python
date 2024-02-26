# 0404 - Sum of Left Leaves
# Date: 2022-11-18
# Runtime: 41 ms, Memory: 14.8 MB
# Submission Id: 845722166


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def traverse(node, is_left):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans += node.val if is_left else 0
            if node.left:
                traverse(node.left, True)
            if node.right:
                traverse(node.right, False)
                
        traverse(root, False)
        return ans