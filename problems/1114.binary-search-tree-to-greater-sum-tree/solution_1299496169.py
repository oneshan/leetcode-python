# 1114 - Binary Search Tree to Greater Sum Tree
# Date: 2024-06-25
# Runtime: 35 ms, Memory: 16.5 MB
# Submission Id: 1299496169


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        stack = []
        
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            total = node.val = total + node.val

            node = node.left

        return root