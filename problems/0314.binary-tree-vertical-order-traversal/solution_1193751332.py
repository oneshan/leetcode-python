# 0314 - Binary Tree Vertical Order Traversal
# Date: 2024-03-04
# Runtime: 42 ms, Memory: 16.6 MB
# Submission Id: 1193751332


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
        while queue:
            node, idx = queue.popleft()
            table[idx].append(node.val)
            if node.left:
                queue.append((node.left, idx-1))
            if node.right:
                queue.append((node.right, idx+1))

        ans = []
        for i in range(-100, 101):
            if table[i]:
                ans.append(table[i])
        return ans