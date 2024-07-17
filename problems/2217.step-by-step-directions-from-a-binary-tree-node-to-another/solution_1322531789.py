# 2217 - Step-By-Step Directions From a Binary Tree Node to Another
# Date: 2024-07-16
# Runtime: 229 ms, Memory: 52.2 MB
# Submission Id: 1322531789


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
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

        path_s, path_d = [], []
        get_path(root, startValue, path_s)
        get_path(root, destValue, path_d)

        i = j = 0
        while i < len(path_s) and j < len(path_d) and path_s[i] == path_d[j]:
            i += 1
            j += 1
        
        return 'U' * (len(path_s) - i) + ''.join(path_d[j:])