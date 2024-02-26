# 0095 - Unique Binary Search Trees II
# Date: 2023-08-05
# Runtime: 64 ms, Memory: 17.9 MB
# Submission Id: 1012589168


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def recur(left, right):
            if left > right:
                return [None]
            
            arr = []
            for i in range(left, right+1):
                left_trees = recur(left, i-1)
                right_trees = recur(i+1, right)
                for l in left_trees:
                    for r in right_trees:
                        arr.append(TreeNode(i, l, r))
            return arr
            
        return recur(1, n)