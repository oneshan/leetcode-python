# 1114 - Binary Search Tree to Greater Sum Tree
# Date: 2024-06-25
# Runtime: 34 ms, Memory: 16.4 MB
# Submission Id: 1299492591


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def inorder(node):
            if not node:
                return
            inorder(node.right)
            node.val = self.sum = self.sum + node.val
            inorder(node.left)

        inorder(root)
        return root