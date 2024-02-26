# 0112 - Path Sum
# Date: 2022-10-23
# Runtime: 64 ms, Memory: 15 MB
# Submission Id: 828505473


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, 0)]
        while stack:
            node, curr_sum = stack.pop()
            curr_sum += node.val
            if not node.left and not node.right and curr_sum == targetSum:
                return True
            if node.left: stack.append((node.left, curr_sum))
            if node.right: stack.append((node.right, curr_sum))
        return False