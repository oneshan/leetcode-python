# 0652 - Find Duplicate Subtrees
# Date: 2022-07-17
# Runtime: 111 ms, Memory: 26.8 MB
# Submission Id: 749473894


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.seen = {}
        self.ans = set()
        self.traverse(root)
        return [self.seen[pattern] for pattern in self.ans]
    
    def traverse(self, node):
        if not node:
            return "#"
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        
        pattern = f'{node.val}:[{left}:{right}]'
        if pattern in self.seen:
            self.ans.add(pattern)
        self.seen[pattern] = node
        return pattern