# 0105 - Construct Binary Tree from Preorder and Inorder Traversal
# Date: 2024-05-22
# Runtime: 49 ms, Memory: 18.1 MB
# Submission Id: 1264621408


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        mapping = {val: idx for idx, val in enumerate(inorder)}
        self.pid = 0

        def recur(left, right):
            if left > right:
                return None
            val = preorder[self.pid]
            mid = mapping[val]
            self.pid += 1            

            node = TreeNode(val)
            node.left = recur(left, mid-1)
            node.right = recur(mid+1, right)
            return node

        return recur(0, len(preorder)-1)