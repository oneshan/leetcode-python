# 0513 - Find Bottom Left Tree Value
# Date: 2024-02-28
# Runtime: 32 ms, Memory: 18.2 MB
# Submission Id: 1188264663


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root)])
        ans = None
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                ans = node.val
        return ans