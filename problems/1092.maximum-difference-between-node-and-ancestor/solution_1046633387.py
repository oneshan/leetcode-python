# 1092 - Maximum Difference Between Node and Ancestor
# Date: 2023-09-11
# Runtime: 44 ms, Memory: 22.5 MB
# Submission Id: 1046633387


class Solution:
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        
        def dfs(node, curr_max, curr_min):
            if not node:
                return curr_max - curr_min
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            left = dfs(node.left, curr_max, curr_min)
            right = dfs(node.right, curr_max, curr_min)
            return max(left, right)
        
        return dfs(root, root.val, root.val)