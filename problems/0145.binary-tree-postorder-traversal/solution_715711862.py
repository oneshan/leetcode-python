# 0145 - Binary Tree Postorder Traversal
# Date: 2022-06-06
# Runtime: 57 ms, Memory: 13.7 MB
# Submission Id: 715711862


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.traverse(root, ans)
        return ans
    
    def traverse(self, node, ans):
        if not node:
            return
        self.traverse(node.left, ans)
        self.traverse(node.right, ans)
        ans.append(node.val)