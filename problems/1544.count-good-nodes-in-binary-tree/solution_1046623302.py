# 1544 - Count Good Nodes in Binary Tree
# Date: 2023-09-11
# Runtime: 192 ms, Memory: 35.4 MB
# Submission Id: 1046623302


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0
        
        def recur(node, curr_max):
            nonlocal ans
            if not node:
                return
            if node.val >= curr_max:
                ans += 1
            curr_max = max(curr_max, node.val)
            recur(node.left, curr_max)
            recur(node.right, curr_max)
            
        recur(root, root.val)
        return ans