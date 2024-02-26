# 0543 - Diameter of Binary Tree
# Date: 2023-01-02
# Runtime: 41 ms, Memory: 16.2 MB
# Submission Id: 869495015


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