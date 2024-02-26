# 0515 - Find Largest Value in Each Tree Row
# Date: 2023-09-12
# Runtime: 54 ms, Memory: 18.8 MB
# Submission Id: 1046655516


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        while queue:
            curr_max = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curr_max)
        return ans