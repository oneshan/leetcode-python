# 1035 - Cousins in Binary Tree
# Date: 2024-04-17
# Runtime: 36 ms, Memory: 16.5 MB
# Submission Id: 1234987975


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([(root, None)])

        px = py = None
        while queue:
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                if node.val == x:
                    px = parent
                elif node.val == y:
                    py = parent
                if node.left:
                    queue.append((node.left, node.val))
                if node.right:
                    queue.append((node.right, node.val))
            if px and py:
                return px != py
            if px or py:
                return False
        return False