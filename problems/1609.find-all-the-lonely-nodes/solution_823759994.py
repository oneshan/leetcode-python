# 1609 - Find All The Lonely Nodes
# Date: 2022-10-16
# Runtime: 111 ms, Memory: 15.2 MB
# Submission Id: 823759994


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def recursion(node):
            if not node:
                return
            if bool(node.left) ^ bool(node.right):
                ans.append((node.left or node.right).val)
            recursion(node.left)
            recursion(node.right)
        
        recursion(root)
        return ans