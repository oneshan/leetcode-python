# 0094 - Binary Tree Inorder Traversal
# Date: 2022-06-06
# Runtime: 55 ms, Memory: 13.9 MB
# Submission Id: 715707707


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.traverse(root, ans)
        return ans
    
    def traverse(self, node, ans):
        if not node:
            return
        self.traverse(node.left, ans)
        ans.append(node.val)
        self.traverse(node.right, ans)