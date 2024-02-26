# 0501 - Find Mode in Binary Search Tree
# Date: 2023-11-01
# Runtime: 60 ms, Memory: 20.6 MB
# Submission Id: 1088803238


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        freq = defaultdict(int)
        stack = [root]
        while stack:
            node = stack.pop()
            freq[node.val] += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        max_freq = max(freq.values())
        return [node for node, count in freq.items() if count == max_freq]