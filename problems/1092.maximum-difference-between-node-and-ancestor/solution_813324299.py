# 1092 - Maximum Difference Between Node and Ancestor
# Date: 2022-10-02
# Runtime: 84 ms, Memory: 20 MB
# Submission Id: 813324299


class Solution:
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        return self.dfs(root, root.val, root.val)
        
    def dfs(self, node, curr_max, curr_min):
        if not node:
            return curr_max - curr_min
        curr_max = max(curr_max, node.val)
        curr_min = min(curr_min, node.val)
        left = self.dfs(node.left, curr_max, curr_min)
        right = self.dfs(node.right, curr_max, curr_min)
        return max(left, right)