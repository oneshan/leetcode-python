# 0199 - Binary Tree Right Side View
# Date: 2022-10-02
# Runtime: 42 ms, Memory: 13.9 MB
# Submission Id: 813498071


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
        
        ans = []
        queue = deque([root])
        while queue:
            level_nodes = len(queue)
            for _ in range(level_nodes):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(node.val)
        return ans