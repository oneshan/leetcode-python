# 0101 - Symmetric Tree
# Date: 2024-02-15
# Runtime: 36 ms, Memory: 16.5 MB
# Submission Id: 1175733606


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root, root])
        while queue:
            n1, n2 = queue.popleft(), queue.popleft()
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