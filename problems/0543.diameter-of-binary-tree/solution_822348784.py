# 0543 - Diameter of Binary Tree
# Date: 2022-10-14
# Runtime: 119 ms, Memory: 16.3 MB
# Submission Id: 822348784


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        table = {}
        stack = [root]
        seen = set()
        while stack:
            node = stack.pop()
            if node in seen:
                left = table.get(node.left, 0)
                right = table.get(node.right, 0)
                ans = max(ans, left+right)
                table[node] = max(left, right) + 1
            else:
                seen.add(node)
                stack.append(node)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return ans