# 1092 - Maximum Difference Between Node and Ancestor
# Date: 2022-10-02
# Runtime: 105 ms, Memory: 20 MB
# Submission Id: 813322356


class Solution:
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        self.ans = 0
        self.dfs(root, root.val, root.val)
        return self.ans
        
    def dfs(self, node, curr_max, curr_min):
        if not node:
            return
        self.ans = max(self.ans, curr_max-node.val, node.val-curr_min)
        curr_max = max(curr_max, node.val)
        curr_min = min(curr_min, node.val)
        self.dfs(node.left, curr_max, curr_min)
        self.dfs(node.right, curr_max, curr_min)