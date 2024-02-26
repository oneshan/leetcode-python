# 0652 - Find Duplicate Subtrees
# Date: 2023-02-28
# Runtime: 56 ms, Memory: 16.4 MB
# Submission Id: 906333061


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        table = defaultdict(int)
        triplet_to_id = {}
        ans = []
        
        def recur(node):
            if not node:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            triplet = (left, node.val, right)
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            triplet_id = triplet_to_id[triplet]
            
            if table[triplet_id] == 1:
                ans.append(node)
            table[triplet_id] += 1
            return triplet_id
        
        recur(root)
        return ans