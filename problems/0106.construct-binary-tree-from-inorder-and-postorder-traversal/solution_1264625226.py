# 0106 - Construct Binary Tree from Inorder and Postorder Traversal
# Date: 2024-05-22
# Runtime: 46 ms, Memory: 18.2 MB
# Submission Id: 1264625226


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapping = {val: idx for idx, val in enumerate(inorder)}
        self.pid = len(inorder) - 1

        def recur(left, right):
            if left > right:
                return None
            
            val = postorder[self.pid]
            mid = mapping[val]
            self.pid -= 1

            node = TreeNode(val)
            node.right = recur(mid+1, right)
            node.left = recur(left, mid-1)
            return node

        return recur(0, len(inorder)-1)