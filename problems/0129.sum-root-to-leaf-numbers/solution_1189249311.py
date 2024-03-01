# 0129 - Sum Root to Leaf Numbers
# Date: 2024-02-29
# Runtime: 38 ms, Memory: 16.5 MB
# Submission Id: 1189249311


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        queue = deque([(root, 0)])
        while queue:
            node, curr_sum = queue.popleft()
            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right:
                ans += curr_sum
                continue
            if node.left:
                queue.append((node.left, curr_sum))
            if node.right:
                queue.append((node.right, curr_sum))
        return ans