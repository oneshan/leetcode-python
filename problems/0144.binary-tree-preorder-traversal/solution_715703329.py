# 0144 - Binary Tree Preorder Traversal
# Date: 2022-06-06
# Runtime: 63 ms, Memory: 13.8 MB
# Submission Id: 715703329


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.traverse(root, ans)
        return ans
    
    def traverse(self, node, ans):
        if not node:
            return None
        ans.append(node.val)
        self.traverse(node.left, ans)
        self.traverse(node.right, ans)
        