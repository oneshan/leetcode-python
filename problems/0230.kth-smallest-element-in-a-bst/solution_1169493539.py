# 0230 - Kth Smallest Element in a BST
# Date: 2024-02-08
# Runtime: 54 ms, Memory: 19.4 MB
# Submission Id: 1169493539


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = 0

        def inorder(node):
            if not node or self.count == k:
                return
            inorder(node.left)

            self.count += 1
            if self.count == k:
                self.ans = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.ans