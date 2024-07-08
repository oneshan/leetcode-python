# 1450 - Delete Leaves With a Given Value
# Date: 2024-05-17
# Runtime: 45 ms, Memory: 17.1 MB
# Submission Id: 1260406868


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
                
        stack = []
        last_right = None
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack[-1]

            if node.right and node.right != last_right:
                node = node.right
                continue
            
            stack.pop()

            if not node.right and not node.left and node.val == target:
                if not stack:
                    return None
                parent = stack[-1]
                if parent.left == node:
                    parent.left = None
                if parent.right == node:
                    parent.right = None

            last_right = node
            node = None
        
        return root