# 0515 - Find Largest Value in Each Tree Row
# Date: 2022-10-02
# Runtime: 109 ms, Memory: 17.1 MB
# Submission Id: 813505277


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.ans = []
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, node, level):
        if level == len(self.ans):
            self.ans.append(node.val)
        self.ans[level] = max(self.ans[level], node.val)
        if node.left: self.dfs(node.left, level+1)
        if node.right: self.dfs(node.right, level+1)