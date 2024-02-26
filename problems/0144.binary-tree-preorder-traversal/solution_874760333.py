# 0144 - Binary Tree Preorder Traversal
# Date: 2023-01-09
# Runtime: 36 ms, Memory: 13.8 MB
# Submission Id: 874760333


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        
        def traverse(node):
            if not node:
                return
            self.ans.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return self.ans