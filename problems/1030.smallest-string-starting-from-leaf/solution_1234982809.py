# 1030 - Smallest String Starting From Leaf
# Date: 2024-04-17
# Runtime: 48 ms, Memory: 18.1 MB
# Submission Id: 1234982809


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        ans = ''
        queue = deque([(root, '')])
        while queue:
            node, curr = queue.popleft()
            curr = chr(node.val + ord('a')) + curr
            if not node.left and not node.right:
                ans = min(ans, curr) if ans else curr
            if node.left:
                queue.append((node.left, curr))
            if node.right:
                queue.append((node.right, curr))
        return ans