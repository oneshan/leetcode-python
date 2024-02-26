# 0904 - Leaf-Similar Trees
# Date: 2024-01-09
# Runtime: 35 ms, Memory: 17.3 MB
# Submission Id: 1140950718


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return 
            if not node.left and not node.right:
                yield node.val
            yield from traverse(node.left)
            yield from traverse(node.right)
            
        return list(traverse(root1)) == list(traverse(root2))