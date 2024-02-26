# 1544 - Count Good Nodes in Binary Tree
# Date: 2022-10-02
# Runtime: 371 ms, Memory: 32.7 MB
# Submission Id: 813260414


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        self.dfs(root, float('-inf'))
        return self.ans
    
    def dfs(self, node, curr_max):
        if not node:
            return
        if node.val >= curr_max:
            self.ans += 1
        if node.left:
            self.dfs(node.left, max(curr_max,node.val))
        if node.right:
            self.dfs(node.right, max(curr_max,node.val))
        