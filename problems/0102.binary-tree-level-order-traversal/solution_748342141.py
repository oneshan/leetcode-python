# 0102 - Binary Tree Level Order Traversal
# Date: 2022-07-16
# Runtime: 65 ms, Memory: 14.2 MB
# Submission Id: 748342141


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
        
        ans, queue = [], deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return ans