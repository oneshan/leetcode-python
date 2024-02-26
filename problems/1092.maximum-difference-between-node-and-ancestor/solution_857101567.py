# 1092 - Maximum Difference Between Node and Ancestor
# Date: 2022-12-09
# Runtime: 98 ms, Memory: 19.9 MB
# Submission Id: 857101567


class Solution:
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        
        def dfs(node, curr_min, curr_max):
            if not node:
                return
            self.ans = max(self.ans, abs(curr_max-node.val), abs(node.val-curr_min))
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            dfs(node.left, curr_min, curr_max)
            dfs(node.right, curr_min, curr_max)
        
        self.ans = 0
        dfs(root, root.val, root.val)
        return self.ans