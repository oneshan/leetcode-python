# 1092 - Maximum Difference Between Node and Ancestor
# Date: 2022-12-09
# Runtime: 65 ms, Memory: 19.9 MB
# Submission Id: 857102078


class Solution:
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        
        def dfs(node, curr_min, curr_max):
            if not node:
                return curr_max - curr_min
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            left = dfs(node.left, curr_min, curr_max)
            right = dfs(node.right, curr_min, curr_max)
            return max(left, right)
        
        self.ans = 0
        return dfs(root, root.val, root.val)