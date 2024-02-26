# 0102 - Binary Tree Level Order Traversal
# Date: 2024-02-13
# Runtime: 40 ms, Memory: 17.2 MB
# Submission Id: 1173855972


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = deque([root])
        while queue:
            ans.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                ans[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans