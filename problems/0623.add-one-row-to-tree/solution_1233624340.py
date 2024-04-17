# 0623 - Add One Row to Tree
# Date: 2024-04-16
# Runtime: 54 ms, Memory: 17.8 MB
# Submission Id: 1233624340


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        def recur(node, depth):
            if not node:
                return
            if depth > 2:
                recur(node.left, depth-1)
                recur(node.right, depth-1)
            else:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)

        recur(root, depth)
        return root