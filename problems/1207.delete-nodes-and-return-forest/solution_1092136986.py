# 1207 - Delete Nodes And Return Forest
# Date: 2023-11-06
# Runtime: 66 ms, Memory: 16.9 MB
# Submission Id: 1092136986


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        ans = []
        stack = [(root, False)]
        while stack:
            node, parent_exist = stack.pop()
            if node is None:
                continue
            if node.val in to_delete:
                stack.append((node.left, False))
                stack.append((node.right, False))
                continue
            if not parent_exist:
                ans.append(node)

            if node.left:
                stack.append((node.left, True))
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                stack.append((node.right, True))
                if node.right.val in to_delete:
                    node.right = None
        return ans