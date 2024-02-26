# 0784 - Insert into a Binary Search Tree
# Date: 2023-10-01
# Runtime: 112 ms, Memory: 19.1 MB
# Submission Id: 1064012609


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        prev, curr = None, root
        while curr:
            prev = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        
        if not prev:
            return TreeNode(val)
        if prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        return root