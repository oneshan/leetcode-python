# 0094 - Binary Tree Inorder Traversal
# Date: 2022-10-22
# Runtime: 55 ms, Memory: 14 MB
# Submission Id: 827945558


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        
        def recur(node):
            if not node:
                return
            recur(node.left)
            ans.append(node.val)
            recur(node.right)
            
        recur(root)
        return ans