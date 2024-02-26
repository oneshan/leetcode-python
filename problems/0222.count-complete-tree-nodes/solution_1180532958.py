# 0222 - Count Complete Tree Nodes
# Date: 2024-02-20
# Runtime: 63 ms, Memory: 21.7 MB
# Submission Id: 1180532958


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        depth, node = 0, root
        while node.left:
            node = node.left
            depth += 1

        def is_exist(idx):
            node = root
            left, right = 0, (1 << depth)-1
            while left < right:
                mid = (left + right) // 2
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return bool(node)

        left, right = 1, (1 << depth)
        while left < right:
            mid = (left + right) // 2
            if is_exist(mid):
                left = mid + 1
            else:
                right = mid
        return (1 << depth)-1 + left