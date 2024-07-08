# 2416 - Evaluate Boolean Binary Tree
# Date: 2024-05-16
# Runtime: 51 ms, Memory: 16.9 MB
# Submission Id: 1259276778


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        TRUE, FALSE, OR, AND = 1, 0, 2, 3

        stack = [root]
        evaluated = {}

        while stack:
            node = stack[-1]   
              
            if not node.left and not node.right:
                stack.pop()
                evaluated[node] = node.val
                continue
            
            if node.left in evaluated and node.right in evaluated:
                stack.pop()
                if node.val == AND:
                    evaluated[node] = evaluated[node.left] and evaluated[node.right]
                else:
                    evaluated[node] = evaluated[node.left] or evaluated[node.right]
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return evaluated[root]