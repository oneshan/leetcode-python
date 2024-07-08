# 1544 - Count Good Nodes in Binary Tree
# Date: 2024-05-14
# Runtime: 126 ms, Memory: 31.6 MB
# Submission Id: 1257821351


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = [(root, root.val)]
        ans = 0
        while stack:
            node, curr_max = stack.pop()
            if node.val >= curr_max:
                ans += 1
            curr_max = max(curr_max, node.val)
            if node.left:
                stack.append((node.left, curr_max))
            if node.right:
                stack.append((node.right, curr_max))
        return ans
