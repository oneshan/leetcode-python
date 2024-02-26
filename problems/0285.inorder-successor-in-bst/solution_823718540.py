# 0285 - Inorder Successor in BST
# Date: 2022-10-16
# Runtime: 184 ms, Memory: 18.9 MB
# Submission Id: 823718540


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        ans = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                ans = root
                root = root.left
        return ans