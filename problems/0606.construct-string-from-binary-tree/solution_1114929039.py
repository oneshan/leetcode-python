# 0606 - Construct String from Binary Tree
# Date: 2023-12-08
# Runtime: 54 ms, Memory: 18.4 MB
# Submission Id: 1114929039


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        stack = [root]
        ans = []
        visited = set()
        
        while stack:
            node = stack[-1]
            if node in visited:
                stack.pop()
                ans.append(')')
            else:
                visited.add(node)
                ans.append('(')
                ans.append(str(node.val))
                if not node.left and node.right:
                    ans.append('(')
                    ans.append(')')
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return ''.join(ans[1:-1])