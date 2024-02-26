# 0784 - Insert into a Binary Search Tree
# Date: 2023-09-16
# Runtime: 124 ms, Memory: 19 MB
# Submission Id: 1050232861


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        node = root
        while node:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                node = node.left
        return root