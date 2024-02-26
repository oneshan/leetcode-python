# 0095 - Unique Binary Search Trees II
# Date: 2022-10-28
# Runtime: 147 ms, Memory: 15.8 MB
# Submission Id: 832064770


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []
        return self.genBST(1, n)

    def genBST(self, left, right):
        if left > right:
            return [None]
        
        arr = []
        for i in range(left, right + 1):
            left_trees = self.genBST(left, i-1)
            right_trees = self.genBST(i+1, right)
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    arr.append(root)
        return arr