# 0226 - Invert Binary Tree
# Date: 2022-10-02
# Runtime: 59 ms, Memory: 13.9 MB
# Submission Id: 813284925


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        
        root.right = left
        root.left = right
        return root