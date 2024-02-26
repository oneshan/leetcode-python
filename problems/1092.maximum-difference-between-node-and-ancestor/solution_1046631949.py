# 1092 - Maximum Difference Between Node and Ancestor
# Date: 2023-09-11
# Runtime: 48 ms, Memory: 22.3 MB
# Submission Id: 1046631949


class Solution:
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        
        ans = 0
        def dfs(node, curr_max, curr_min):
            nonlocal ans
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            ans = max(ans, curr_max - curr_min)
            if node.left:
                dfs(node.left, curr_max, curr_min)
            if node.right:
                dfs(node.right, curr_max, curr_min)
        
        dfs(root, root.val, root.val)
        return ans