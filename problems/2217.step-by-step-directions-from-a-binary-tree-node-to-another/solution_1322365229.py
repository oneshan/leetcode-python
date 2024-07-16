# 2217 - Step-By-Step Directions From a Binary Tree Node to Another
# Date: 2024-07-16
# Runtime: 239 ms, Memory: 52.2 MB
# Submission Id: 1322365229


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find_lca(root, p, q):
            if not root:
                return None
            if root.val == p or root.val == q:
                return root
            left = find_lca(root.left, p, q)
            right = find_lca(root.right, p, q)
            if left and right:
                return root
            return left or right

        def get_path(root, p, path):
            if not root:
                return False
            if root.val == p:
                return True
            
            path.append('L')
            if get_path(root.left, p, path):
                return True
            path.pop()

            path.append('R')
            if get_path(root.right, p, path):
                return True
            path.pop()

            return False

        lca = find_lca(root, startValue, destValue)

        res = []
        get_path(lca, startValue, res)
        res = ['U' for _ in range(len(res))]
        get_path(lca, destValue, res)
        return ''.join(res)