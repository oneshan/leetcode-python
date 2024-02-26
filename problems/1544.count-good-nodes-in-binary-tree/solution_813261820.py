# 1544 - Count Good Nodes in Binary Tree
# Date: 2022-10-02
# Runtime: 488 ms, Memory: 32.6 MB
# Submission Id: 813261820


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        stack = [(root, float('-inf'))]
        while stack:
            node, curr_max = stack.pop()
            if node.val >= curr_max:
                ans += 1
            if node.left: stack.append((node.left, max(curr_max, node.val)))
            if node.right: stack.append((node.right, max(curr_max, node.val)))
        return ans