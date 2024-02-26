# 0094 - Binary Tree Inorder Traversal
# Date: 2022-05-11
# Runtime: 37 ms, Memory: 13.9 MB
# Submission Id: 697459988


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans
    
    def helper(self, node, ans):
        if not node:
            return
        self.helper(node.left, ans)
        ans.append(node.val)
        self.helper(node.right, ans)