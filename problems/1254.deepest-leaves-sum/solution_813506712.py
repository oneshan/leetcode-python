# 1254 - Deepest Leaves Sum
# Date: 2022-10-02
# Runtime: 474 ms, Memory: 17.9 MB
# Submission Id: 813506712


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        while queue:
            level_nodes = len(queue)
            curr_sum = 0
            for _ in range(level_nodes):
                node = queue.popleft()
                curr_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return curr_sum