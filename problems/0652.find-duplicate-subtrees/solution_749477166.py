# 0652 - Find Duplicate Subtrees
# Date: 2022-07-17
# Runtime: 93 ms, Memory: 26.7 MB
# Submission Id: 749477166


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.seen = {}
        self.ans = []
        self.traverse(root)
        return self.ans
    
    def traverse(self, node):
        if not node:
            return "#"
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        
        pattern = f'{node.val}:[{left}:{right}]'
        self.seen[pattern] = self.seen.get(pattern, 0) + 1        
        if self.seen[pattern] == 2:
            self.ans.append(node)
        return pattern