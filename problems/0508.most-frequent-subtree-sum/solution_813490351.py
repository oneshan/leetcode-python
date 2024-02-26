# 0508 - Most Frequent Subtree Sum
# Date: 2022-10-02
# Runtime: 117 ms, Memory: 17.6 MB
# Submission Id: 813490351


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.table = defaultdict(int)
        self.dfs(root)
        
        max_count = max(self.table.values())
        return [key for key in self.table if self.table[key] == max_count]
        
    
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        curr_sum = left + right + node.val
        self.table[curr_sum] += 1
        return curr_sum