# 0930 - All Possible Full Binary Trees
# Date: 2023-07-23
# Runtime: 206 ms, Memory: 26 MB
# Submission Id: 1001467048


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
        if n == 1:
            return [TreeNode()]
        
        ans = []
        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n-i-1)
            
            for l in left:
                for r in right:
                    ans.append(TreeNode(0, l, r))
        return ans