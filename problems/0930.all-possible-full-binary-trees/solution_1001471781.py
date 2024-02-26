# 0930 - All Possible Full Binary Trees
# Date: 2023-07-23
# Runtime: 173 ms, Memory: 19.5 MB
# Submission Id: 1001471781


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        dp = [[] for _ in range(n+1)]
        dp[1].append(TreeNode())
        
        for count in range(3, n+1, 2):
            for i in range(1, count-1, 2):
                j = count - 1 - i
                for left in dp[i]:
                    for right in dp[j]:
                        dp[count].append(TreeNode(0, left, right))
        return dp[n]