# 1474 - Longest ZigZag Path in a Binary Tree
# Date: 2023-04-19
# Runtime: 514 ms, Memory: 61.6 MB
# Submission Id: 936115237


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def recur(node, go_left, count):
            if not node:
                return
            self.ans = max(self.ans, count)
            if go_left:
                recur(node.left, True, 1)
                recur(node.right, False, count + 1)
            else:
                recur(node.left, True, count + 1)
                recur(node.right, False, 1)

        recur(root, False, 0)
        recur(root, True, 0)
        return self.ans