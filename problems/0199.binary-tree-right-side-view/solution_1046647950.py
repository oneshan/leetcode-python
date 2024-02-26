# 0199 - Binary Tree Right Side View
# Date: 2023-09-11
# Runtime: 43 ms, Memory: 16.2 MB
# Submission Id: 1046647950


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        while queue:
            ans.append(None)
            for _ in range(len(queue)):
                node = queue.popleft()
                ans[-1] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans