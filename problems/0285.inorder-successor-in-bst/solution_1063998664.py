# 0285 - Inorder Successor in BST
# Date: 2023-10-01
# Runtime: 76 ms, Memory: 20.8 MB
# Submission Id: 1063998664


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # case1. parent
        # case2. parent -> leftmost node
        ans, curr = None, root
        while curr:
            if p.val < curr.val:
                ans = curr
                curr = curr.left
            else:
                curr = curr.right
        return ans