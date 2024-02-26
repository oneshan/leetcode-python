# 0508 - Most Frequent Subtree Sum
# Date: 2022-10-02
# Runtime: 77 ms, Memory: 17.6 MB
# Submission Id: 813487963


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
        ans_list, ans_count = [], 0
        for key, val in self.table.items():
            if val > ans_count:
                ans_list = [key]
                ans_count = val
            elif val == ans_count:
                ans_list.append(key)
        return ans_list
        
    
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        curr_sum = left + right + node.val
        self.table[curr_sum] += 1
        return curr_sum