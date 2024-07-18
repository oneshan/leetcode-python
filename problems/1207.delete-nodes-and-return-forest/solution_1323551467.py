# 1207 - Delete Nodes And Return Forest
# Date: 2024-07-17
# Runtime: 44 ms, Memory: 17.1 MB
# Submission Id: 1323551467


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []

        def dfs(node, has_parent):
            if not node:
                return

            if node.val not in to_delete and has_parent is False:
                res.append(node)

            has_parent = False if node.val in to_delete else True
            
            if node.left:
                dfs(node.left, has_parent)
                if node.left.val in to_delete:
                    node.left = None

            if node.right:
                dfs(node.right, has_parent)
                if node.right.val in to_delete:
                    node.right = None

        dfs(root, False)
        return res