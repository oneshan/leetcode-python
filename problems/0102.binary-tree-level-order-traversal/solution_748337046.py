# 0102 - Binary Tree Level Order Traversal
# Date: 2022-07-16
# Runtime: 71 ms, Memory: 14.9 MB
# Submission Id: 748337046


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.recursion(root, 0)
        return self.ans
        
    def recursion(self, node, level):
        if not node:
            return
        if len(self.ans) < level + 1:
            self.ans.append([])
        self.ans[level].append(node.val)
        self.recursion(node.left, level+1)
        self.recursion(node.right, level+1)