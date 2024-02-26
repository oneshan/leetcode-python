# 0102 - Binary Tree Level Order Traversal
# Date: 2022-10-22
# Runtime: 74 ms, Memory: 14.2 MB
# Submission Id: 827957177


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        while queue:
            ans.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                ans[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans