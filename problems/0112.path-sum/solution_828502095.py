# 0112 - Path Sum
# Date: 2022-10-23
# Runtime: 67 ms, Memory: 15 MB
# Submission Id: 828502095


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
        
        ans = False
        def recur(node, curr_sum):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans |= curr_sum + node.val == targetSum
                return
            recur(node.left, curr_sum+node.val)
            recur(node.right, curr_sum+node.val)
        
        recur(root, 0)
        return ans