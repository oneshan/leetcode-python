# 2217 - Step-By-Step Directions From a Binary Tree Node to Another
# Date: 2022-10-22
# Runtime: 1712 ms, Memory: 137.8 MB
# Submission Id: 827796260


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.route = []
        
        def find_lca(node):
            if not node:
                return None
            if node.val in (startValue, destValue):
                return node
                
            left = find_lca(node.left)
            right = find_lca(node.right)
            if left and right:
                return node
            return left or right
        
        def traverse(node, target, path, upper):
            if not node:
                return
            if node.val == target:
                self.route.extend(path)
                return
            path.append('U' if upper else 'R')
            traverse(node.right, target, path, upper)
            path.pop()
            
            path.append('U' if upper else 'L')
            traverse(node.left, target, path, upper)
            path.pop()

            
        lca = find_lca(root)
        traverse(lca, startValue, [], upper=True)
        traverse(lca, destValue, [], upper=False)
        return ''.join(self.route)