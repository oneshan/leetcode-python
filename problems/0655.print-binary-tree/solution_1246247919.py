# 0655 - Print Binary Tree
# Date: 2024-05-01
# Runtime: 44 ms, Memory: 16.6 MB
# Submission Id: 1246247919


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        len_r = get_height(root)
        len_c = 2 ** len_r - 1
        ans = [ [''] * len_c for _ in range(len_r)]

        def recur(node, r, c):
            ans[r][c] = str(node.val)
            if node.left:
                recur(node.left, r+1, c - 2 ** (len_r - r - 2))
            if node.right:
                recur(node.right, r+1, c + 2 ** (len_r - r - 2))

        recur(root, 0, (2 ** len_r - 2) // 2)
        return ans