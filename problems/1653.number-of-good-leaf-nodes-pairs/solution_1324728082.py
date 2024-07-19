# 1653 - Number of Good Leaf Nodes Pairs
# Date: 2024-07-18
# Runtime: 80 ms, Memory: 16.9 MB
# Submission Id: 1324728082


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def dfs(node):
            nonlocal ans

            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for d1 in left:
                for d2 in right:
                    if d1 + d2 <= distance:
                        ans += 1
            
            return [1+d for d in left + right if 1+d < distance]

        
        ans = 0
        dfs(root)
        return ans