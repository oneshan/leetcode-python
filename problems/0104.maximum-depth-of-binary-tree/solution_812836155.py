# 0104 - Maximum Depth of Binary Tree
# Date: 2022-10-02
# Runtime: 73 ms, Memory: 15.3 MB
# Submission Id: 812836155


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(1, root)]
        ans = 0
        while stack:
            depth, node = stack.pop()
            if node:
                ans = max(ans, depth)
                stack.append((depth+1, node.left))
                stack.append((depth+1, node.right))
        return ans