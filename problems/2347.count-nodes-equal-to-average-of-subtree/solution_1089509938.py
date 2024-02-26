# 2347 - Count Nodes Equal to Average of Subtree
# Date: 2023-11-02
# Runtime: 51 ms, Memory: 17.8 MB
# Submission Id: 1089509938


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def recur(node):
            nonlocal ans
            
            if not node:
                return 0, 0
            left_sum, left_count = recur(node.left)
            right_sum, right_count = recur(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            if total_sum // total_count == node.val:
                ans += 1
            return (total_sum, total_count)
        
        recur(root)
        return ans
            