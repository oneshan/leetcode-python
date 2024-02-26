# 1544 - Count Good Nodes in Binary Tree
# Date: 2022-10-02
# Runtime: 550 ms, Memory: 33.1 MB
# Submission Id: 813265646


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        queue = deque([(root, float('-inf'))])
        while queue:
            node, curr_max = queue.popleft()
            if node.val >= curr_max:
                ans += 1
            if node.left: queue.append((node.left, max(curr_max, node.val)))
            if node.right: queue.append((node.right, max(curr_max, node.val)))
        return ans