# 1544 - Count Good Nodes in Binary Tree
# Date: 2022-12-06
# Runtime: 256 ms, Memory: 32.5 MB
# Submission Id: 855467619


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def traverse(node, curr_max):
            nonlocal count
            if not node:
                return
            if node.val >= curr_max:
                count += 1
                curr_max = node.val
            traverse(node.left, curr_max)
            traverse(node.right, curr_max)      
                
        traverse(root, float('-inf'))
        return count