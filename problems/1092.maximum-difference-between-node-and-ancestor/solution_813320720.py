# 1092 - Maximum Difference Between Node and Ancestor
# Date: 2022-10-02
# Runtime: 77 ms, Memory: 14.8 MB
# Submission Id: 813320720


class Solution:
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        
        stack = [(root, root.val, root.val)]
        ans = 0
        while stack:
            node, curr_max, curr_min = stack.pop()
            ans = max(ans, curr_max-node.val, node.val-curr_min)
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            if node.left:
                stack.append((node.left, curr_max, curr_min))
            if node.right:
                stack.append((node.right, curr_max, curr_min))
        return ans