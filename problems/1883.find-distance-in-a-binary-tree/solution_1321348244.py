# 1883 - Find Distance in a Binary Tree
# Date: 2024-07-15
# Runtime: 54 ms, Memory: 20.7 MB
# Submission Id: 1321348244


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        def find_lca(node, p, q):
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            left = find_lca(node.left, p, q)
            right = find_lca(node.right,p, q)
            if left and right:
                return node
            return left or right

        def get_dist(node, target):
            if not node:
                return float('inf')
            if node.val == target:
                return 0
            return 1 + min(get_dist(node.left, target), get_dist(node.right, target))

        # calulate lca->p + lca->q
        node = find_lca(root, p, q)
        return get_dist(node, p) + get_dist(node, q)