# 0257 - Binary Tree Paths
# Date: 2022-12-06
# Runtime: 58 ms, Memory: 14 MB
# Submission Id: 855455700


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        if not root:
            return []
        
        def traverse(node, path):
            if not node.left and not node.right:
                ans.append('->'.join(path))
                return
            if node.left:
                path.append(str(node.left.val))
                traverse(node.left, path)
                path.pop()
            if node.right:
                path.append(str(node.right.val))
                traverse(node.right, path)
                path.pop()
        
        traverse(root, [str(root.val)])
        return ans