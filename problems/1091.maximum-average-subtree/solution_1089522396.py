# 1091 - Maximum Average Subtree
# Date: 2023-11-02
# Runtime: 59 ms, Memory: 19.2 MB
# Submission Id: 1089522396


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ans = 0
        
        def recur(node):
            nonlocal ans
            
            if not node:
                return 0, 0
            l_sum, l_count = recur(node.left)
            r_sum, r_count = recur(node.right)
            
            total_sum = l_sum + r_sum + node.val
            total_count = l_count + r_count + 1
            
            ans = max(ans, total_sum / total_count)
            return total_sum, total_count
        
        recur(root)
        return ans