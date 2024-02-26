# 1609 - Find All The Lonely Nodes
# Date: 2022-10-16
# Runtime: 116 ms, Memory: 14.3 MB
# Submission Id: 823758608


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            stack.append(node.left)
            stack.append(node.right)
            if bool(node.left) ^ bool(node.right):
                tmp = node.left or node.right
                ans.append(tmp.val)
        return ans