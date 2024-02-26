# 0543 - Diameter of Binary Tree
# Date: 2023-10-10
# Runtime: 42 ms, Memory: 18.6 MB
# Submission Id: 1071795204


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0
        def helper(node):
            nonlocal ans
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            ans = max(ans, left + right)
            return max(left, right) + 1
        
        helper(root)
        return ans