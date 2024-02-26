# 1544 - Count Good Nodes in Binary Tree
# Date: 2023-09-11
# Runtime: 198 ms, Memory: 35.3 MB
# Submission Id: 1046621716


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        queue = deque()
        queue.append((root, root.val))
        ans = 0
        while queue:
            node, curr_max = queue.popleft()
            if node.val >= curr_max:
                ans += 1
            curr_max = max(curr_max, node.val)
            if node.left:
                queue.append((node.left, curr_max))
            if node.right:
                queue.append((node.right, curr_max))
        return ans