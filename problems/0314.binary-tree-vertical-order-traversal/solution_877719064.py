# 0314 - Binary Tree Vertical Order Traversal
# Date: 2023-01-14
# Runtime: 41 ms, Memory: 13.8 MB
# Submission Id: 877719064


from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        table = defaultdict(list)
        queue = deque([(root, 0)])
        left = right = 0
        while queue:
            node, column = queue.popleft()
            left, right = min(left, column), max(right, column)
            table[column].append(node.val)
            if node.left:
                queue.append((node.left, column-1))
            if node.right:
                queue.append((node.right, column+1))
        
        return [table[i] for i in range(left, right+1)]