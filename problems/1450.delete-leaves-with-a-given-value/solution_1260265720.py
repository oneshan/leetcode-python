# 1450 - Delete Leaves With a Given Value
# Date: 2024-05-17
# Runtime: 48 ms, Memory: 17.2 MB
# Submission Id: 1260265720


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def recur(node):
            if not node:
                return None
            node.left = recur(node.left)
            node.right = recur(node.right)
            if not node.left and not node.right and node.val == target:
                return None
            return node

        return recur(root)