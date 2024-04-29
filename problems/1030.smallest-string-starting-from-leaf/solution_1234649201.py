# 1030 - Smallest String Starting From Leaf
# Date: 2024-04-17
# Runtime: 39 ms, Memory: 17.8 MB
# Submission Id: 1234649201


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        self.ans = None

        def recur(node, path):
            if not node:
                return []
            path.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                if not self.ans:
                    self.ans = ''.join(path[::-1])
                else:
                    self.ans = min(self.ans, ''.join(path[::-1]))
            recur(node.left, path)
            recur(node.right, path)
            path.pop()
        
        recur(root, [])
        return self.ans