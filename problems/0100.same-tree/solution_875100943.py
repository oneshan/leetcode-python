# 0100 - Same Tree
# Date: 2023-01-10
# Runtime: 42 ms, Memory: 13.9 MB
# Submission Id: 875100943


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val
        
        queue = deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not check(n1, n2):
                return False
            if n1:
                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))
        return True