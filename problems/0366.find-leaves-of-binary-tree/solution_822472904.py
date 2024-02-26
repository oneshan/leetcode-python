# 0366 - Find Leaves of Binary Tree
# Date: 2022-10-15
# Runtime: 64 ms, Memory: 14 MB
# Submission Id: 822472904


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def traverse(node):
            nonlocal ans
            
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            
            level = max(left, right) + 1
            if len(ans) < level:
                ans.append([])
            ans[level-1].append(node.val)
            return level
        
        traverse(root)
        return ans