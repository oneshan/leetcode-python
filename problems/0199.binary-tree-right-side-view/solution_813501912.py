# 0199 - Binary Tree Right Side View
# Date: 2022-10-02
# Runtime: 70 ms, Memory: 13.9 MB
# Submission Id: 813501912


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
        
        self.ans = []
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, node, level):
        if level == len(self.ans):
            self.ans.append(node.val)
        if node.right: self.dfs(node.right, level+1)
        if node.left: self.dfs(node.left, level+1)