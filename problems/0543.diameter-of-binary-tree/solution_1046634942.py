# 0543 - Diameter of Binary Tree
# Date: 2023-09-11
# Runtime: 38 ms, Memory: 18.7 MB
# Submission Id: 1046634942


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