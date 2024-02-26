# 0100 - Same Tree
# Date: 2022-07-21
# Runtime: 35 ms, Memory: 13.9 MB
# Submission Id: 752156014


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
        
        if not p and not q:
            return True
        if not check(p, q):
            return False
        queue_p, queue_q = deque(), deque()
        queue_p.append(p)
        queue_q.append(q)
        while queue_p and queue_q:
            p = queue_p.popleft()
            q = queue_q.popleft()
            if not check(p.left, q.left) or not check(p.right, q.right):
                return False
            if p.left:
                queue_p.append(p.left)
                queue_q.append(q.left)
            if p.right:
                queue_p.append(p.right)
                queue_q.append(q.right)
        return True