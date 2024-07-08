# 0933 - Increasing Order Search Tree
# Date: 2024-06-09
# Runtime: 44 ms, Memory: 16.5 MB
# Submission Id: 1282884516


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.dummy = self.curr = TreeNode()

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            root.left = None
            self.curr.right = root
            self.curr = root
            inorder(root.right)

        inorder(root)
        return self.dummy.right