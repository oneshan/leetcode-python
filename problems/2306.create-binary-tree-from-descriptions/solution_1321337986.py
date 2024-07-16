# 2306 - Create Binary Tree From Descriptions
# Date: 2024-07-15
# Runtime: 1569 ms, Memory: 25.8 MB
# Submission Id: 1321337986


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mapping = {}
        children = set()

        for parent, child, is_left in descriptions:
            children.add(child)
            if child not in mapping:
                mapping[child] = TreeNode(child)
            if parent not in mapping:
                mapping[parent] = TreeNode(parent)
            if is_left:
                mapping[parent].left = mapping[child]
            else:
                mapping[parent].right = mapping[child]

        for key, node in mapping.items():
            if key not in children:
                return node
        return None