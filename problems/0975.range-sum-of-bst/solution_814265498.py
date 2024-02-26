# 0975 - Range Sum of BST
# Date: 2022-10-03
# Runtime: 248 ms, Memory: 23.1 MB
# Submission Id: 814265498


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ans += node.val
            if node.left and node.val > low:
                stack.append(node.left)
            if node.right and node.val < high:
                stack.append(node.right)
        return ans