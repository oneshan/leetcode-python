# 0404 - Sum of Left Leaves
# Date: 2022-11-18
# Runtime: 29 ms, Memory: 14.1 MB
# Submission Id: 845724676


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                if node.left.right is None and node.left.left is None:
                    ans += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans