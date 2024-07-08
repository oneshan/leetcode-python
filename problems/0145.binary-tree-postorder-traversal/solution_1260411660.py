# 0145 - Binary Tree Postorder Traversal
# Date: 2024-05-17
# Runtime: 39 ms, Memory: 16.4 MB
# Submission Id: 1260411660


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        stack = []
        node = root

        last_right = None
        res = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack[-1]
            if node.right and node.right != last_right:
                node = node.right
                continue

            temp = stack.pop()
            res.append(temp.val)
            last_right = node
            node = None
        
        return res