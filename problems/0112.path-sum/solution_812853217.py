# 0112 - Path Sum
# Date: 2022-10-02
# Runtime: 92 ms, Memory: 14.9 MB
# Submission Id: 812853217


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
        
        stack = [(root, targetSum - root.val)]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
        return False