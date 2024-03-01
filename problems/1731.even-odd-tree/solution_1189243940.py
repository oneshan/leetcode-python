# 1731 - Even Odd Tree
# Date: 2024-02-29
# Runtime: 208 ms, Memory: 37.9 MB
# Submission Id: 1189243940


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0

        queue = deque([root])
        while queue:
            prev = 0 if level & 1 == 0 else 1_000_001
            for _ in range(len(queue)):
                node = queue.popleft()
                if level & 1 and (node.val >= prev or node.val & 1):
                    return False
                if level & 1 == 0 and (node.val <= prev or node.val & 1 == 0):
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node.val
            level ^= 1
        return True