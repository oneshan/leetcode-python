# 0101 - Symmetric Tree
# Date: 2022-10-23
# Runtime: 57 ms, Memory: 14 MB
# Submission Id: 828498544


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root, root])
        while queue:
            n1 = queue.popleft()
            n2 = queue.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            queue.append(n1.left)
            queue.append(n2.right)
            queue.append(n1.right)
            queue.append(n2.left)
        return True